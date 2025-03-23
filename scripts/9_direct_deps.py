import re
import json
from pathlib import Path

def handle_empty_file(filename):
    """Process empty files using filename pattern"""
    filename_base = Path(filename).name
    name = re.sub(r'_cgraph\.dot$', '', filename_base)
    return {name: []}

def handle_non_empty_file(content):
    """Original processing logic for files with content"""
    digraph_match = re.search(r'digraph\s+"([^"]+)"', content)
    if not digraph_match:
        raise ValueError("No digraph name found in file content")
    digraph_name = digraph_match.group(1)
    
    nodes = dict(re.findall(r'(\w+)\s*\[\s*label="([^"]+)"', content))
    edges = re.findall(r'(\w+)\s*->\s*(\w+)', content)
    
    main_node_id = next((nid for nid, label in nodes.items() 
                        if label == digraph_name), None)
    
    dependencies = []
    if main_node_id:
        for src, tgt in edges:
            if src == main_node_id and tgt in nodes:
                dependencies.append(nodes[tgt])
    
    return {digraph_name: dependencies}

def analyze_dot_dependencies(filename):
    """Main analysis router"""
    with open(filename, 'r') as f:
        content = f.read().strip()

    return handle_empty_file(filename) if not content else handle_non_empty_file(content)

if __name__ == "__main__":
    results = {}
    src_dir = Path("src")

    # Find all _cgraph.dot files recursively in src directory
    dot_files = src_dir.glob('**/*_cgraph.dot')

    for dot_file in dot_files:
        try:
            result = analyze_dot_dependencies(dot_file)
            results.update(result)
            print(f"Processed: {dot_file}")
        except Exception as e:
            print(f"Error processing {dot_file}: {str(e)}")
    
    with open('output/direct_deps.json', 'w') as f:
        json.dump(results, f, indent=2)
    
    print("Dependency analysis completed. Results saved to direct_deps.json")

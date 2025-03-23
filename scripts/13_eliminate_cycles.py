import json

# Load adjacency list from JSON file

with open('output/direct_deps_number_format.json', 'r') as file:
    adjacency_list = json.load(file)

def remove_cycles(graph):
    visited = set()
    merged_nodes_log = []
    cycles = []  # List to store detected cycles

    def dfs(node, path):
        if node in path:  # Cycle detected
            cycle_start_index = path.index(node)
            cycles.append(path[cycle_start_index:])
            return

        if node in visited:
            return

        visited.add(node)
        path.append(node)

        for neighbor in graph.get(node, []):
            dfs(str(neighbor), path)

        path.pop()

    # Detect cycles using DFS
    for node in graph.keys():
        if node not in visited:
            dfs(node, [])

    # Merge nodes involved in cycles
    for cycle_nodes in cycles:
        merged_key = cycle_nodes[0]  # Use first node as merged key
        merged_values = set()

        for cycle_node in cycle_nodes:
            merged_values.update(graph.get(cycle_node, []))
            if cycle_node != merged_key:
                del graph[cycle_node]

        merged_values.discard(int(merged_key))
        graph[merged_key] = list(merged_values)
        merged_nodes_log.append({"merged_key": merged_key, "merged_nodes": cycle_nodes})

    return graph, merged_nodes_log

# Remove cycles and log merged nodes
updated_adjacency_list, merged_log = remove_cycles(adjacency_list)

# Save updated adjacency list to file
with open('output/acyclic_direct_deps_numeric.json', 'w') as file:
    json.dump(updated_adjacency_list, file, indent=4)

# Save log of merged nodes to JSON file
with open('logs/merged_nodes.json', 'w') as log_file:
    json.dump(merged_log, log_file, indent=4)

print("Updated adjacency list saved to 'output/acyclic_direct_deps_numeric.json'.")
print("Merged nodes log saved to 'logs/merged_nodes.json'.")

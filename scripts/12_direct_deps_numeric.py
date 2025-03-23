import json
from pathlib import Path

def convert_dependencies_to_numbers():    
    with open('routine_2_number_mapping.json', 'r') as f:
        routine_to_num = json.load(f)

    # Load original dependencies
    with open('output/direct_deps.json', 'r') as f:
        name_based_deps = json.load(f)

    number_based_deps = {}
    missing_deps = set()

    for routine_name, dependencies in name_based_deps.items():
        # Convert main routine name to number
        try:
            routine_num = routine_to_num[routine_name]
        except KeyError:
            print(f"Warning: {routine_name} not found in mapping, skipping")
            missing_deps.add(routine_name)
            continue

        # Convert dependencies to numbers
        numbered_deps = []
        for dep in dependencies:
            try:
                numbered_deps.append(routine_to_num[dep])
            except KeyError:
                print(f"Warning: Dependency {dep} for {routine_name} not found, skipping")
                missing_deps.add(dep)
        
        number_based_deps[routine_num] = numbered_deps

    # Save numbered dependencies
    with open('output/direct_deps_number_format.json', 'w') as f:
        json.dump(number_based_deps, f, indent=2, sort_keys=True)

    # Save unique missing dependencies
    with open('logs/missing.json', 'w') as f:
        json.dump(list(missing_deps), f, indent=2)

    print("Successfully created direct_deps_number_format.json")
    print(f"Logged {len(missing_deps)} unique missing entries in missing.json")

if __name__ == "__main__":
    convert_dependencies_to_numbers()

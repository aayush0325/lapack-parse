import json
from pathlib import Path

def create_routine_number_mapping():
    # Get the path to the src directory
    src_dir = Path("src")

    # Get all immediate subdirectories of src
    routines = [folder.name for folder in src_dir.iterdir() if folder.is_dir()]

    # Sort the routines alphabetically to ensure consistent numbering
    routines.sort()

    # Create the mapping
    routine_mapping = {routine: i for i, routine in enumerate(routines)}

    # Save the mapping to a JSON file
    with open('output/routine_2_number_mapping.json', 'w') as f:
        json.dump(routine_mapping, f, indent=2)

    print(f"Mapping created and saved to routine_2_number_mapping.json")
    print(f"Total number of routines mapped: {len(routines)}")

if __name__ == "__main__":
    create_routine_number_mapping()

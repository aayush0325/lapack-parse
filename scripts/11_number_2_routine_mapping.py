import json
from pathlib import Path

def create_inverse_mapping():
    try:
        # Load original mapping
        with open('output/routine_2_number_mapping.json', 'r') as f:
            original_mapping = json.load(f)
        
        # Create inverse mapping with integer keys
        inverse_mapping = {v: k for k, v in original_mapping.items()}
        
        # Save inverse mapping
        with open('output/number_2_routine_mapping.json', 'w') as f:
            json.dump(inverse_mapping, f, indent=2, sort_keys=True)
        
        print("Successfully created number_2_routine_mapping.json")
        print(f"Mapped {len(inverse_mapping)} entries")

    except FileNotFoundError:
        print("Error: routine_2_number_mapping.json not found")
    except json.JSONDecodeError:
        print("Error: Invalid JSON format in input file")
    except Exception as e:
        print(f"Unexpected error: {str(e)}")

if __name__ == "__main__":
    create_inverse_mapping()

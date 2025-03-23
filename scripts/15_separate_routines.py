import json

# Load the original list from WORKING_ORDER.json
with open('output/WORKING_ORDER.json', 'r') as file:
    working_order = json.load(file)

# Initialize dictionaries for each category
single_precision = []
double_precision = []
single_precision_complex = []
double_precision_complex = []
misc = []

# Categorize based on the prefix of the routine name
for routine in working_order:
    if routine.startswith('s'):
        single_precision.append(routine)
    elif routine.startswith('d'):
        double_precision.append(routine)
    elif routine.startswith('c'):
        single_precision_complex.append(routine)
    elif routine.startswith('z'):
        double_precision_complex.append(routine)
    else:
        misc.append(routine)

# Save each category into its respective JSON file
output_files = {
    "SINGLE_PRECISION_WORKING_ORDER.json": single_precision,
    "DOUBLE_PRECISION_WORKING_ORDER.json": double_precision,
    "SINGLE_PRECISION_COMPLEX_WORKING_ORDER.json": single_precision_complex,
    "DOUBLE_PRECISION_COMPLEX_WORKING_ORDER.json": double_precision_complex,
    "MISC_WORKING_ORDER.json": misc
}

for filename, data in output_files.items():
    with open(f'output/{filename}', 'w') as file:
        json.dump(data, file, indent=4)

print("Files have been successfully created and categorized!")

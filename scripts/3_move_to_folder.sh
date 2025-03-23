#!/bin/bash

# Collect all unique base names
declare -A base_names
for file in *_cgraph.dot *_icgraph.dot; do
    # Extract the base name by removing _cgraph.dot or _icgraph.dot
    base_name=$(echo "$file" | sed -E 's/(.+)_(c|ic)graph\.dot$/\1/')
    base_names["$base_name"]=1
done

# Process each unique base name
echo "Moving files to their respective directories..."
dir_count=0
file_count=0

for base_name in "${!base_names[@]}"; do
    # Create directory if it doesn't exist
    if [ ! -d "$base_name" ]; then
        mkdir -p "$base_name"
        echo "Created directory: $base_name"
        ((dir_count++))
    fi
    
    # Move cgraph file if it exists
    if [ -f "${base_name}_cgraph.dot" ]; then
        mv "${base_name}_cgraph.dot" "$base_name/"
        echo "Moved: ${base_name}_cgraph.dot to $base_name/"
        ((file_count++))
    fi

    # Move icgraph file if it exists
    if [ -f "${base_name}_icgraph.dot" ]; then
        mv "${base_name}_icgraph.dot" "$base_name/"
        echo "Moved: ${base_name}_icgraph.dot to $base_name/"
        ((file_count++))
    fi
done

echo "Done. Created $dir_count directories and moved $file_count files."
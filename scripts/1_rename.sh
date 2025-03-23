#!/bin/bash

# Check if there are any matching files
if ! ls *_8f*_cgraph.dot *_8f*_icgraph.dot 2>/dev/null; then
    echo "No matching files found."
    exit 1
fi

# Process each file matching the patterns
for file in *_8f*_cgraph.dot *_8f*_icgraph.dot; do
    routine_name=$(echo "$file" | sed -E 's/(.+)_8f.+_(c|ic)graph\.dot/\1/')
    
    if [[ "$file" == *_cgraph.dot ]]; then
        graph_type="cgraph"
    else
        graph_type="icgraph"
    fi
    
    new_file="${routine_name}_${graph_type}.dot"
    
    echo "Renaming: $file -> $new_file"
    mv "$file" "$new_file"
done

echo "File renaming complete."
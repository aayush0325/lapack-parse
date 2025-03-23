#!/bin/bash

# Check if there are any dot files
if ! ls *_cgraph.dot *_icgraph.dot 2>/dev/null; then
    echo "No *_cgraph.dot or *_icgraph.dot files found in current directory."
    exit 1
fi

echo "Checking for missing counterpart files..."
created_count=0

# Process all cgraph files first
for file in *_cgraph.dot; do
    base_name=$(echo "$file" | sed 's/_cgraph\.dot$//')
    
    counterpart="${base_name}_icgraph.dot"
    if [ ! -f "$counterpart" ]; then
        touch "$counterpart"
        echo "Created empty file: $counterpart"
        ((created_count++))
    fi
done

# Process all icgraph files next
for file in *_icgraph.dot; do
    base_name=$(echo "$file" | sed 's/_icgraph\.dot$//')
    
    counterpart="${base_name}_cgraph.dot"
    if [ ! -f "$counterpart" ]; then
        touch "$counterpart"
        echo "Created empty file: $counterpart"
        ((created_count++))
    fi
done

echo "Done. Created $created_count missing counterpart files."
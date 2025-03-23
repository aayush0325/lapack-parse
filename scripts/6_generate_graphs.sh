#!/bin/bash

echo "Generating PNG graphs for each folder in src/ except VARIANTS_FOLDER..."
processed_count=0
error_count=0

# Process each directory inside src/
for dir in src/*/; do
    # Remove trailing slash and get just the directory name
    dir=${dir%/}
    dir_name=$(basename "$dir")

    # Skip if this is VARIANTS_FOLDER
    if [ "$dir_name" = "VARIANTS_FOLDER" ]; then
        echo "Skipping: src/$dir_name (excluded)"
        continue
    fi

    echo "Processing folder: src/$dir_name"

    # Check for cgraph.dot file
    cgraph_file=$(find "$dir" -name "*_cgraph.dot" -type f | head -n 1)
    if [ -n "$cgraph_file" ]; then
        # Generate dependencies graph
        echo "Generating dependencies.png from $(basename "$cgraph_file")"

        if dot -T png "$cgraph_file" -o "$dir/img/dependencies.png"; then
            echo "Created $dir/img/dependencies.png"
        else
            echo "Error generating dependencies.png"
            ((error_count++))
        fi
    else
        echo "  ! No *_cgraph.dot file found in $dir"
        ((error_count++))
    fi
    
    # Check for icgraph.dot file
    icgraph_file=$(find "$dir" -name "*_icgraph.dot" -type f | head -n 1)
    if [ -n "$icgraph_file" ]; then
        # Generate dependents graph
        echo "  Generating dependents.png from $(basename "$icgraph_file")"
        if dot -T png "$icgraph_file" -o "$dir/img/dependents.png"; then
            echo "Created $dir/img/dependents.png"
        else
            echo "Error generating dependents.png"
            ((error_count++))
        fi
    else
        echo "  ! No *_icgraph.dot file found in $dir"
        ((error_count++))
    fi
    
    ((processed_count++))
    echo ""
done

echo "Done. Processed $processed_count folders."
if [ $error_count -gt 0 ]; then
    echo "Warning: Encountered $error_count errors during processing."
fi
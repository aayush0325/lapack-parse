#!/bin/bash

echo "Creating img directories in all folders inside src/ except VARIANTS_FOLDER..."
created_count=0

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

    # Create img directory inside the current directory if it doesn't exist
    if [ ! -d "$dir/img" ]; then
        mkdir -p "$dir/img"
        echo "Created: src/$dir_name/img/"
        ((created_count++))
    else
        echo "Skipping: src/$dir_name/img/ (already exists)"
    fi
done

echo "Done. Created img directories in $created_count folders within src/."
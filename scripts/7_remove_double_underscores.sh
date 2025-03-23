#!/bin/bash

echo "Looking for directories with double underscores..."
renamed_count=0

# Find all directories and check if they have double underscores
for dir in src/*/; do
    # Remove trailing slash
    dir=${dir%/}
    
    # Check if the directory name contains double underscores
    if [[ "$dir" == *__* ]]; then
        # Create new name with single underscores
        new_name=$(echo "$dir" | sed 's/__/_/g')
        
        # Rename the directory
        mv "$dir" "$new_name"
        echo "Renamed: $dir → $new_name"
        ((renamed_count++))
    fi
done

if [ $renamed_count -eq 0 ]; then
    echo "No directories with double underscores found."
else
    echo "Done. Renamed $renamed_count directories."
fi
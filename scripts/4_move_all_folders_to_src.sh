#!/bin/bash

# Create src directory if it doesn't exist
if [ ! -d "src" ]; then
    mkdir -p src
    echo "Created src directory"
fi

echo "Moving directories to src/..."
moved_count=0

# Process each directory
for dir in $dirs; do
    # Get just the directory name without the ./ prefix
    dir_name=$(basename "$dir")

    # Move the directory to src
    mv "$dir_name" "src/"
    echo "Moved: $dir_name to src/$dir_name"
    ((moved_count++))
done

echo "Done. Moved $moved_count directories to src/."
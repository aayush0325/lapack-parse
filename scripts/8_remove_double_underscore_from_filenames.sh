#!/bin/bash

find src -depth -name "*__*" -print0 | while IFS= read -r -d '' file; do
    mv -v "$file" "${file//__/_}"
done

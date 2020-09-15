#!/bin/bash

# Coder: Aleksander Aleksiev 
# Listener: Yang Xiang
# Sharer: ChunChao Tseng

# Using find
# find . -type f -executable

# Using for loop
for file in $( ls ); do
    if [ -x $file ]; then 
        echo "$file is executable."
    fi
done
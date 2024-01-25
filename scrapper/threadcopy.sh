#!/bin/bash


if [ -f "threads.txt" ]; then

    if [ -d "data/" ]; then

        cp threads.txt data/
        echo "thread.txt has been copied to ../../data/"
    else
        echo "Directory data/ does not exist."
    fi
else
    echo "File threads.txt does not exist."
fi

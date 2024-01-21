#!/bin/bash


if [ -f "thread.txt" ]; then

    if [ -d "../../data/" ]; then

        cp thread.txt ../../data/
        echo "thread.txt has been copied to ../../data/"
    else
        echo "Directory ../../data/ does not exist."
    fi
else
    echo "File thread.txt does not exist."
fi
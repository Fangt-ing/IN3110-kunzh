#!/bin/bash
function movefls () {
    if [ -d "$1" ] && [ -d "$2" ]; then # -d: FILE exists and is a directory
        ls "./$1"
        mv "$1"/* "$2"
        echo "Files from $1 are moved to $2"
    elif [ -d "$1" ] && [ ! -d "$2" ]; then
        echo "The destination directory does not exist!"
    elif [ ! -d "$1" ] && [ -d "$2" ]; then
        echo "The source directory does not exist!"
    elif [ ! -d "$1" ] && [ ! -d "$2" ]; then
        echo "Both the soure and the destination directory do not exist!"
    fi
}

movefls "$1" "$2"
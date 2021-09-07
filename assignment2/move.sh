#!/bin/bash
function move() {
    if [ -n "$1" ] && [ -n "$2" ]; then # -n: length of the string is a non-zero.
        echo "$# directories are indicated."
        ls "./$1" # list all the files in the src folder.
        mv "$1"/* "$2" # move all files to the dst folder.
        echo "Files from $1 are moved to $2."
    elif [[ -n "$1" && -z "$2" ]]; then # -z: check if the input string length is zero or not.
        echo "$# directories are indicated."
        echo "The destination directory does not exist!"
    elif [ -z "$1" ]; then # regardless of $2, if $1 is empty, then comes the elif
        echo "$# directories are indicated."
        echo "Both the soure and the destination directory do not exist!"
    fi
}

move $1 $2
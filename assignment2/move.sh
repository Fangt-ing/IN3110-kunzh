#!/bin/bash

#$1 or number aftert the $ is for being excuted in bash order.
src=$1
dst=$2
filetypes=$3

# move certain types of file works as the following.
# src=$1, dst=$2, ft=$3
# mv $src/*.$ft $dst

if [ $# -ge 2 ]; then
    echo "There are $# arguments."
    if [ -d $src ]; then
        if [ -d "$dst" ]; then
            if [ -n "$filetypes" ]; then
                echo $filetypes
                # mv $src/*.$filetyps $dst
                find $src -name "*.$filetypes" -exec mv "{}" $dst \;
                echo "All $filetypes files are moved."
            elif [ -z "$filetypes" ]; then
                mv $src/* $dst
                echo "All content in folder $src are moved to folder $dst."
            fi
        elif [ ! -d "$dst" ]; then
            echo "The folder $dst does not exist, do you want to create one?"
            echo "y/Yes/Y or no/No/n/N"
            read dirname
            if [ $dirname = "y" ] || [ $dirname = "Yes" ] || [ $dirname = "Y" ]; then
                echo "Do you want to append the current time to your directory name?"
                echo "y/Yes/Y or no/No/n/N"
                read appendtime
                if [ $appendtime = "y" ] || [ $appendtime = "Yes" ] || [ $appendtime = "Y" ]; then
                    mkdir $dst-$(date +"%Y-%h-%d_%H:%M")
                    echo "The destination folder $dst-$(date +"%Y-%h-%d_%H:%M") is created."
                elif [ $appendtime = "no" ] || [ $appendtime = "No" ] || [ $appendtime = "n" ] || [ $appendtime = "N" ]; then
                    mkdir $dst
                    echo "The destination folder $dst is created."
                fi
            elif [ $dirname = "no" ] || [ $dirname = "No" ] || [ $dirname = "n" ] || [ $dirname = "N" ]; then
                echo "The destination folder $dst is not created."
            else
                echo "You did not enter a correct answer, the operation is aborted."
            fi
        fi
    else
        echo "The source folder does not exist."
        echo "The operation is aborted."
    fi

# the following block describe the situations when arguments are less than 2. ie. 0 and 1.
elif [ 2 -gt $# ]; then
    if [ -d "$src" ]; then
        echo "The source folder $src exist, but your argument input is only $#."
        echo "There has to be at least 2 arguments."
    elif [ ! -d $src ]; then
        echo "The source folder $src does not exist."
    fi

    echo "You argument input is only $#."
    echo "There has to be at least 2 arguments."
elif [ -z $src ]; then
    echo "You argument input is only $#."
    echo "There has to be at least 2 arguments."
fi

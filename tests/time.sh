#!/bin/bash

trackORnot="$1"

if [ "$1" = "start" ]; then
    date
    tracking=1
    echo "tacking time."
elif [ "$1" = "stop" ]; then
    date
    tracking=0
    echo "time tracking stopped."
else
    echo "the track is not started."
fi

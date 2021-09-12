#!/bin/bash

function latch() {
    running=false
    if [ $running = true ]; then
        echo "something is running."
        running=false
        echo $running
    elif [ $running = false ]; then
        echo "something is not running."
        running=true
        echo $running
    fi
}

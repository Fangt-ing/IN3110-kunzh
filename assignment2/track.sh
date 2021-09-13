#!/bin/bash

source ~/.bashrc

running=false
task=$1
label=$2

st="start_time"
et="end_time"

# date | cut -d' ' -f2-3
# Sep 2021

function writelog() {

    if [ "$task" = "start" ]; then
        if [ -n "$label" ]; then
            st=$(date +"%a %b %d %T %Z %Y")
            echo "START " $st >>"$LOGFILE"
            echo "LABEL This is $label" >>"$LOGFILE"
        elif [ -z "$label" ]; then
            echo "Please provide a task lable/name. Syntax is 'track start task_lable/name'."
        fi
    elif [ "$task" = "stop" ]; then
        et=$(date +"%a %b %d %T %Z %Y")
        echo "END " $et >>"$LOGFILE" #$'\n'
    fi
}

function track() {
    task=$1
    label=$2
    stat=$(tail -1 ~/.local/share/.timer_logfile)
    if [ "$task" = "start" ]; then
        if [ $running = false ]; then
            writelog "$task" "$label"
            running=true
            labelname=$(tail -1 ~/.local/share/.timer_logfile | cut -d' ' -f4)
        elif [ $running = true ]; then
            echo "$stat" #| cut -d' ' -f2-)"."
            echo "Please end the current task by 'track stop' if you wish to start a new tracking task."
        fi
    elif [ "$task" = "stop" ]; then
        if [ $running = true ]; then
            writelog "$task"
            running=false
            duration=$(date -ud@$(($(date -ud "$et" +%s) - $(date -ud "$st" +%s))) +%T)
            echo "$labelname:  $duration" $'\n' >>"$LOGFILE"
        elif [ $running = false ]; then
            echo "There is no tasking running, you may start one using 'track start task-label/name' command."
        fi
    elif [ "$task" = "status" ]; then
        if [ -z "$stat" ]; then
            echo "There is not task running."
            echo "You may use 'track start task-label/name' to start a tracking session."
        else
            echo "$stat" # | cut -d' ' -f2-)"."
        fi
    else
        echo "Please use 'track start task-label/name' to start a tracking session."
        echo "Or use 'track stop' to end a tracking session."
    fi
}
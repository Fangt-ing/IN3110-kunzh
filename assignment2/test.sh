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

# function timelog() {
#     label=$1
#     # starttime="$(date -ud "$st" +%s)" # time convereted into seconds.
#     # endtime="$(date -ud "$et" +%s)" #| cut -d' ' -f4-4)
#     duration=$(date -ud@$(($(date -ud "$et" +%s) - $(date -ud "$st" +%s))) +%T)
#     echo "$label:  $duration" $'\n' >>"$LOGFILE"
# }

# function track() {
#     task=$1
#     label=$2
#     stat=false

#     if [ $(tail -1 logfile.timerlogfile | cut -d' ' -f1-) = "LABEL" ]; then
#         stat=true
#         echo $(tail -1 logfile.timerlogfile | cut -d' ' -f1-) " is running, please stop the task by typing 'stop'."
#         read stop
#         if [ "$stop" = "stop" ]; then
#             stat=false
#         else
#             while [[ $stat = true ]]; do
#                 echo $(tail -1 logfile.timerlogfile | cut -d' ' -f1-) " is running, please stop the task by typing 'stop'."
#                 read stop
#             done
#         fi
#     else
#         if [ ""$task"" = "start" ]; then
#             if [[ "$stat" = false ]]; then
#                 if [ -n "$label" ]; then
#                     echo "START " $(date +"%ae %b %d %T %Z %Y") >>~/.local/share/.timerlogfile
#                     echo "LABEL This is $label" >>~/.local/share/.timerlogfile
#                     stat=true
#                 else
#                     while [ -z "$label" ]; do
#                         echo "Please indicate what task you are working on."
#                         read label
#                     done
#                     echo "START " $(date +"%ae %b %d %T %Z %Y") >>~/.local/share/.timerlogfile
#                     echo "LABEL This is $label" >>~/.local/share/.timerlogfile
#                     stat=true
#                 fi
#             elif [[ "$stat" = true ]]; then
#                 echo $(tail -1 logfile.timerlogfile | cut -d' ' -f2-) "is running, please stop the task first."
#             fi
#         elif [ ""$task"" = "status" ]; then #&& [ -f logfile.timerlogfile ]
#             echo $(tail -1 logfile.timerlogfile | cut -d' ' -f2-) "is running."
#         elif [ ""$task"" = "stop" ]; then
#             if [[ "$stat" = true ]]; then
#                 echo "END " $(date +"%a %b %d %T %Z %Y") "\n" >>~/.local/share/.timerlogfile
#                 stat=false
#             elif [[ "$stat" = false ]]; then
#                 echo "There is no task runnstat, you may type 'track start labelname' to start trackstat time."
#             fi
#         else
#             echo "please indicate a task, to START or END with a LABEL name."
#         fi
#     fi
# }

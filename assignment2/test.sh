#!/bin/bash

task=$1
label=$2

# read task

# if [ "$task" = "start" ]; then
    echo "START " $(date +"%ae %b %d %T %Z %Y") >> $LOGFILE
#     echo "LABEL $label" >> log.txt
# elif [ "$task" = "status" ] && [ -f log.txt ]; then
#     tail -1 $pwd/log.txt
# elif [ "$task" = "end" ]; then
#     echo echo "END " date +"%a %b %d %T %Z %Y" >> log.txt
# else
#     echo "please indicate a task, to START or END with a LABEL name."
# fi

#!/bin/bash

START=$(date +%s);
sleep 1; # Your stuff
END=$(date +%s);
echo $((END-START)) | awk '{print int($1/60)":"int($1%60)}'
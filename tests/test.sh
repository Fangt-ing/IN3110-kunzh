#!/bin/bash

files=($( ls )) #Add () to convert output to array
counter=0
for i in $files ; do
  echo Next: $i
  let counter=$counter+1
  echo $counter
done
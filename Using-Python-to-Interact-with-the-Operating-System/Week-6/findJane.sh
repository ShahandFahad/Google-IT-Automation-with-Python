#!/bin/bash
> oldFiles.txt
files=$(grep " jane " ../data/list.txt | cut -d ' ' -f 3)
for line in $files;do
  echo $HOME$line >> oldFiles.txt 
done
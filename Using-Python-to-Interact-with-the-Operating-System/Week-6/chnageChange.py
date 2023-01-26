#!/usr/bin/env python3
import sys
import subprocess

file = open(sys.argv[1], "r")

for line in file.readlines():
    oldName = line.strip()
    newName = oldName.replace("jane", "jdoe")
    subprocess.run(["mv", oldName, newName])
file.close()

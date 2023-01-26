!/bin/bash

# variable
line="---------------------------------------"

# Script
echo "Starting at: $date "; date; echo $line

echo "UPTIME: "; uptime; echo $line

echo "FREE: "; free; echo $line

echo "WHO: "; who; echo $line

echo "Finishing at:"; date; echo $line


if grep "...."; then echo "....";
else
    echo "......"
fi 

if test -n "...."; then echo "....."; fi 

if [-n $PATH ]; then echo "....."; fi

#  While Loop
n=1
while [ $n -le 5 ]; do
    echo "Iteration $n"
    ((n+=1))
done

# for loop
# renme file with .HTM extension to .html extension
for file in *.HTM; do
    name = $(basename "$file" .HTM)
    mv "$file" "$name.html"
done
#!/bin/bash 

# this
find . -type f | awk '{ print length,$0 }' | sort -h | cat $(awk -F" " '{print $2}')
# OR 
for i in {1..150}; do cat .$(printf '/*%.0s' $(seq $i)) 2>/dev/null; done

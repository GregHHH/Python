#!/usr/bin/env python
import sys

word = ""
sum = 0
# We use the results from mapper.py as input in the Standard Input
for line in sys.stdin:
    # We split the ["word" - "value"] combination into 2 variables
    (key,value) = line.split('\t')
    # If the word is identical to the previous one, we increase sum by 1.
    if word == key:
        sum = sum + int(value)
    else:
        if word != "":
            print(f"{word}  \t  {str(sum)}")
            word = key
            sum = 1
        if key != "": 
            print(f"{key}  \t  {str(sum)}")
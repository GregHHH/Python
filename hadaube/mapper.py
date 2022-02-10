#!/usr/bin/env python
import sys
import string

# We use the file "Zola.txt"as our input. 
for line in sys.stdin:
    # We need to remove whitespaces from the text
    line = line.strip()
    # We remove puntuation from the text
    line = line.translate(str.maketrans('', '', string.punctuation))
    # We create a dict with every words in the File
    words = line.split()
    for word in words:
        print (f"{word}\t{1}")
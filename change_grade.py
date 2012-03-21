#!/usr/bin/env python

import re
import fileinput
from sys import stderr,stdout,argv,exit

if len(argv) != 3:
    stderr.write("Please enter a string and number\n" )
    exit(1)

name = argv[1]
newgrade = argv[2]

for line in fileinput.input('-'):
    m = re.search(name, line)
    values = line.rstrip().split(',') 
    if m:
        values[3] = newgrade
    print ",".join(values)



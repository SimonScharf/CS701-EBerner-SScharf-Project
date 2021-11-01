#!/usr/bin/python3

import sys
import fileinput

if len(sys.argv) < 2:
    print("invalid number of argument provided to tcpOutputParser.\n")
    print(str(sys.argv))
    quit()

for line in fileinput.input():
    if "length" in line:
        content = line.split()
        sourceIP = content[2]
        destIP = content[4][:-1]
        time = content[0]
        size = content[-1]

        print('{:15} s{:20} d{:20} {:8}'.format(time, sourceIP, destIP, size))

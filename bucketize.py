import sys
import os
import fileinput
import math

#we create 20 buckets to allocate packets into
#20 is relatively arbitrary we could use more to potentially increase accuracy
bucketArr = [0]*20
if len(sys.argv) < 2:
    print("too few arguments provided to bucketize.py")
    sys.exit()

filename = str(sys.argv[1])

directory = (str(os.getcwd()))
filePath = directory + "/" + filename


with open (filePath, 'r') as file:
    
    data = file.readlines()

    #if file is empty, we log the error and try next file
    if len(data) < 2:
       print("error: unable to bucketize. " + filename + " is empty.")
       sys.exit()

    startTime = data[0].split()[0]
    endTime = data[-1].split()[0]

    startHr, startMin, startSec = startTime.split(":")
    endHour, endMin, endSec = endTime.split(":")

    msStart = float(startSec) + int(startMin)*60 + int(startHr)*60*60
    msEnd = float(endSec) + int(endMin)*60 + int(endHour)*60*60

    duration = abs(msEnd-msStart)

    #we divide by 19 here because while there are 20 buckets, there are only 19 delimiting points
    bucketSize = duration/19


    for line in fileinput.input(files = filePath):
       time = line.split()[0]
       currentHr, currentMin, currentSec = time.split(":")
       currPacketTime = float(currentSec) + int(currentMin)*60 + int(currentHr)*60*60
       bucketIndex = math.floor((currPacketTime - msStart) / bucketSize)
       bucketArr[bucketIndex] = bucketArr[bucketIndex] + 1 
    
    for bucket in bucketArr:
        print(bucket)



# Script that analyzes cleaned output files and produces combined, averaged file for each website

#dependencies
import os
import fileinput
import time
import sympy
import math
import numpy as np

websites = ["CNN", "Reddit"]
firstTimeValue = 0

for site in websites:
    count_site = [0]*20
    #get full directory paths
    dir = os.getcwd() + "/REQUESTS/" + site + "/DATA"
    
    #use cleaned files only
    for filename in os.listdir(dir):
        count_raw = [0]*20
        if "Cleaned" in filename:
            
            #pattern mechanism
            with open (dir + "/" + filename, 'r') as file:
               data = file.readlines()
               startTime = data[0].split()[0]
               # print(startTime)
               endTime = data[-1].split()[0]
               # print(endTime)
                
               hr1, min1, sec1 = startTime.split(":")
               hr2, min2, sec2 = endTime.split(":")
                
               msStart = float(sec1) + int(min1)*60 + int(hr1)*60*60
               msEnd = float(sec2) + int(min2)*60 + int(hr2)*60*60
                
               duration = abs(msEnd-msStart)
               bucketSize = duration/19
               print("Bucket size is " , bucketSize)
               #totalTime = float(endTime)- float(startTime)

            for line in fileinput.input(files = dir + "/" + filename):
               time = line.split()[0]
               hr3, min3, sec3 = time.split(":")
               msTime = float(sec3) + int(min3)*60 + int(hr3)*60*60
               #print(msTime, msStart)
               bucketFloat = (msTime - msStart) / bucketSize
               bucketIndex = math.floor(bucketFloat)
               count_raw[bucketIndex] = count_raw[bucketIndex] + 1
               #print(count_raw)
               #print(bucketFloat)
               #print(bucketIndex)
            print(count_raw)
            
            #compute average values 
            for i in range(20):
                count_site[i] = round ((count_site[i] + count_raw[i])/2)
    
    np.savetxt(dir + "/" + site + "AverageData.txt", count_site, fmt='%s')

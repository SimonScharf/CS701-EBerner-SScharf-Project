import matplotlib.pyplot as plt
import numpy as np
from matplotlib import collections as matcoll
import fileinput 
import math
import sys

if len(sys.argv) < 4:
    print("invalid number of argument provided to plot.py.\n")
    quit()
    
dataPath = str(sys.argv[1])
websiteName = str(sys.argv[2])
iterationNum = str(sys.argv[3])

x = []
y = []
firstTimeValue = 0

for line in fileinput.input(files = dataPath):
    #fields represents each component of the cleaned data, where the first
    #value is the time, the second is the source ip, the third is the destination ip, and the fourth is the size of the
    #packet
    fields = line.split()
    if len(fields) > 1 and fields[0] != 'we':
        currTime = fields[0].split(":")[2]
        if firstTimeValue == 0:
            firstTimeValue = currTime 
            x.append(0)
        else:
            x.append(float(currTime) - float(firstTimeValue))
            #take log of packet size
        y.append(float(fields[3]))
            #y.append(float(math.log(fields[3]), 10))
print(x)
print(y)

#this is how we add lines instead of points
lines = []
print(len(x))
print(len(y))
for i in range(len(x)):
    pair=[(x[i],0), (x[i], y[i])]
    lines.append(pair)

linecoll = matcoll.LineCollection(lines, linewidth=0.5)
fig, ax = plt.subplots()
ax.add_collection(linecoll)

#these next two lines add x & y axis
#plt.axvline(x=0, c="red", label="x=0")
#plt.axhline(y=0, c="yellow", label="y=0")

plt.scatter(x,y,5)
plt.yscale("symlog")
plt.title(f"{websiteName}{iterationNum}")
plt.xlabel("Time")
plt.ylabel("Packet Size (log)")
plt.savefig(f"REQUESTS/{websiteName}/PLOTS/{websiteName}{iterationNum}.png")
plt.show()

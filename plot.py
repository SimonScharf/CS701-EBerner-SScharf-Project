import matplotlib.pyplot as plt
import numpy as np
from matplotlib import collections as matcoll
import fileinput 

x = []
y = []
firstTimeValue = 0

for line in fileinput.input(files ='tcpCleanedData.txt'):
        #fields represents each component of the cleaned data, where the first
        #value is the time, the second is the packet size, and the third is
        #the direction of the packet (incoming or outgoing)
        fields = line.split()
        if len(fields) > 1 and fields[0] != 'we':
            currTime = fields[0].split(":")[2]
            if firstTimeValue == 0:
                firstTimeValue = currTime 
                x.append(0)
            else:
                x.append(float(currTime) - float(firstTimeValue))
            y.append(float(fields[3]))

print(x)
print(y)

#this is how we add lines instead of points
lines = []
for i in range(len(x)):
    pair=[(x[i],0), (x[i], y[i])]
    lines.append(pair)

linecoll = matcoll.LineCollection(lines)
fig, ax = plt.subplots()
ax.add_collection(linecoll)




#these next two lines add x & y axis
#plt.axvline(x=0, c="red", label="x=0")
#plt.axhline(y=0, c="yellow", label="y=0")

plt.scatter(x,y)
plt.show()

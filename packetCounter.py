import fileinput 
ipDictionary = {}
sumPackets = 0
for line in fileinput.input(files ='tcpCleanedData.txt'):
   content = line.split()
   if not content[1] in ipDictionary: 
       #this means dictionary is currently empty
       ipDictionary[content[1]] = 1 
   if not content[2] in ipDictionary:
       ipDictionary[content[2]] = 1 
   else:
       ipDictionary[content[1]] = ipDictionary[content[1]] + 1
       ipDictionary[content[2]] = int(ipDictionary[content[2]]) + 1
   sumPackets+=1 
print(ipDictionary)
print("total packets: " + str(sumPackets))

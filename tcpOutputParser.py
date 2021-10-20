import fileinput 
for line in fileinput.input(files ='tcpDumpData.txt'):
    if "length" in line:
        
        #get direction, 1 is incoming, -1 is outgoing
        sourceIP = ""
        destIP = ""
        dir = -1
        if "> 10.0." in line:
            dir = 1
        content = line.split()
        sourceIP = content[2]
        destIP = content[4][:-1]
        time = content[0]
        size = content[-1]
        graph_plot = int(content[-1])*dir

        print('{:15} s{:20} d{:20} {:8} {:9}'.format(time, sourceIP, destIP, size, graph_plot))
print("we are done")  

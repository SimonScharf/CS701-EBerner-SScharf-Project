import fileinput 
for line in fileinput.input(files ='tcpDumpData.txt'):
    if "length" in line:
        
        #get direction, 1 is incoming, -1 is outgoing
        dir = -1
        if "> 10.0." in line:
            dir = 1
        content = line.split()
        time = content[0]
        size = content[-1]
        graph_plot = int(content[-1])*dir

        print('{:15} {:8} {:2} {:9}'.format(time, size, dir, graph_plot))
print("we are done")  

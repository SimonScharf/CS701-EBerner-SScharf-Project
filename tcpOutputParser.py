import fileinput 
for line in fileinput.input(files ='tcpDumpData.txt'):
    if "length" in line:
        print(line[0:line.index(' ')] + " ", end='')
        print(line[line.index("length") + 6:])
print("we are done")        

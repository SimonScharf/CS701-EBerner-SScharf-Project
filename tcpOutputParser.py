import fileinput 
for line in fileinput.input(files ='tcpOutput.txt'):
    if "length" in line:
        print(line[0:line.index(' ')] + " ", end='')
        print(line[line.index("length") + 6:])
print("we are done")        

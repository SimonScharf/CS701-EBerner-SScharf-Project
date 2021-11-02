#Script that analyzes averaged pattern files and returns best match
#Only works for CNN, Reddit, and 'other'

#dependencies
import os
import sys
import fileinput

if len(sys.argv) < 2:
    print("invalid parameters provided to patternMatcher.py")
    print(str(sys.argv))
    quit()


known = ["CNN", "Reddit"]

unknownFileArr = []
for line in fileinput.input():
    unknownFileArr.append(int(line))


#unknownFile =  list(map(int,open(os.getcwd() + "/REQUESTS/YouTube/DATA/YouTubeAverageData.txt").read().splitlines()))
#unknownFile = [1, 1, 5, 6, 12, 20, 18, 11, 20, 15, 13, 28, 10, 30, 32, 42, 24, 37, 8, 1]
#print(os.getcwd())


CNNData = list(map(int,open(os.getcwd() + "/REQUESTS/CNN/DATA/CNNAverageData.txt").read().splitlines()))
RedditData = list(map(int,open(os.getcwd() + "/REQUESTS/Reddit/DATA/RedditAverageData.txt").read().splitlines()))

threshold = 50
CNNMatch = 0
RedditMatch = 0

for i in range(len(unknownFileArr)):
    CNNMatch += abs(unknownFileArr[i] - CNNData[i])
    RedditMatch += abs(unknownFileArr[i] - RedditData[i])
print (RedditMatch, CNNMatch)

if CNNMatch < threshold or RedditMatch < threshold:
    if CNNMatch < RedditMatch:
        print("CNN is the closest match")
    else:
        print("Reddit is the closest match")
else:
    print("Neither CNN or Reddit")

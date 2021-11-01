#Script that analyzes averaged pattern files and returns best match
#Only works for CNN, Reddit, and 'other'

#dependencies
import os

known = ["CNN", "Reddit"]

unknownFile = [1, 1, 5, 6, 12, 20, 18, 11, 20, 15, 13, 28, 10, 30, 32, 42, 24, 37, 8, 1]
print(os.getcwd())
CNNData = list(map(int,open(os.getcwd() + "/REQUESTS/CNN/DATA/CNNAverageData.txt").read().splitlines()))
RedditData = list(map(int,open(os.getcwd() + "/REQUESTS/Reddit/DATA/RedditAverageData.txt").read().splitlines()))

CNNMatch = 0
RedditMatch = 0

for i in range(len(unknownFile)):
    if abs(unknownFile[i] - CNNData[i]) < abs(unknownFile[i] - RedditData[i]):
        CNNMatch += 1
    else:
        RedditMatch += 1

if CNNMatch>RedditMatch:
    print("CNN is the closest match")
else:
    print("Reddit is the closest match")

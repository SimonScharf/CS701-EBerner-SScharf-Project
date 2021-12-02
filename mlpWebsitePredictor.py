import joblib
import os
import sys

clf = joblib.load('MLP.model')
#labelArray = ['chase', 'usps', 'wikipedia', 'amazon', 'google', 'indeed', 'youtube', 'ebay', 'cnn', 'nytimes', 'espn', 'paypal', 'imdb', 'reddit', 'zillow']

labelArray = ['wikipedia', 'amazon', 'ebay', 'cnn', 'reddit']
if len(sys.argv) < 2:
    print("invalid number of arguments provided to websitePredictor.py")
    sys.exit()


#with open(os.getcwd() + "/REQUESTS/cnn/DATA/CNNAverageData.txt") as file:
with open(os.getcwd() + "/" + str(sys.argv[1])) as file:
    lines = file.readlines()

    array = [i.strip() for i in lines]
    int_array = [int(numeric_string) for numeric_string in array]

#predict random data
resIndex = clf.predict([int_array])

#translate it to website name
print("This is the predicted website: ")
print(labelArray[resIndex[0]])


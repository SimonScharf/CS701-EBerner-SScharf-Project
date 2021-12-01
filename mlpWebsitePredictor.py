import joblib
import os


clf = joblib.load('MLP.model')

print(dir)
with open(os.getcwd() + "/REQUESTS/cnn/DATA/CNNAverageData.txt") as file:
    lines = file.readlines()
    array = [i.strip() for i in lines]
    print(array)

#predict random data
print(clf.predict([array]))



import numpy as np
from sklearn.feature_extraction import DictVectorizer
from sklearn.model_selection import train_test_split
from sklearn.base import ClassifierMixin
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import Perceptron, LogisticRegression
from sklearn.neural_network import MLPClassifier

# stdlib:
from dataclasses import dataclass
import json
from typing import Dict, Any, List
import random

import os
import fileinput
import time
import math
import numpy as np

firstTimeValue = 0


#%% load up the data
X = []
ys = []


websites = [name for name in os.listdir("./REQUESTS/") if name != '.DS_Store' and name != 'unknown']
#websites = ["cnn", "reddit", "youtube"]

firstTimeValue = 0

for site_index, site in enumerate(websites):
    count_site = [0]*20
    #get full directory paths
    dir = os.getcwd() + "/REQUESTS/" + site + "/DATA"
    
    #use cleaned files only
    for filename in os.listdir(dir):
        bucketArr = [0]*20
        if "Cleaned" in filename:
            
            #pattern mechanism
            with open (dir + "/" + filename, 'r') as file:
               data = file.readlines()
               startTime = data[0].split()[0]
               # print(startTime)
               endTime = data[-1].split()[0]
               # print(endTime)
                
               startHr, startMin, startSec = startTime.split(":")
               endHour, endMin, endSec = endTime.split(":")
                
               msStart = float(startSec) + int(startMin)*60 + int(startHr)*60*60
               msEnd = float(endSec) + int(endMin)*60 + int(endHour)*60*60
                
               duration = abs(msEnd-msStart)
               bucketSize = duration/19
               print("Bucket size is " , bucketSize)
               #totalTime = float(endTime)- float(startTime)

            for line in fileinput.input(files = dir + "/" + filename):
               time = line.split()[0]
               currentHr, currentMin, currentSec = time.split(":")
               currPacketTime = float(currentSec) + int(currentMin)*60 + int(currentHr)*60*60
               bucketIndex = math.floor((currPacketTime - msStart) / bucketSize)
               bucketArr[bucketIndex] = bucketArr[bucketIndex] + 1
               #print(bucketArr)
               #print(bucketFloat)
               #print(bucketIndex)
            print(bucketArr)
            X.append(bucketArr)
            ys.append(site_index)
            #np.savetxt(dir + "/" + site + "IndivBucketData.txt", count_site, fmt='%s')
            
#for _ in range(100):
#  row = [random.randint(1,10) for x in range(20)]
#  X.append(row)
#  ys.append(random.randint(0,9))


X = np.array(X)

print("Features as {} matrix.".format(X.shape))


## SPLIT DATA:

RANDOM_SEED = 12345678

# Numpy-arrays are more useful than python's lists.
y = np.array(ys)
# split off train/validate (tv) pieces.
X_tv, X_test, y_tv, y_test = train_test_split(
    X, y, train_size=0.75, shuffle=True, random_state=RANDOM_SEED
)
# split off train, validate from (tv) pieces.
X_train, X_vali, y_train, y_vali = train_test_split(
    X_tv, y_tv, train_size=0.66, shuffle=True, random_state=RANDOM_SEED
)

print(X_train.shape, X_vali.shape, X_test.shape)

#%% Define & Run Experiments
@dataclass
class ExperimentResult:
    vali_acc: float
    params: Dict[str, Any]
    model: ClassifierMixin


def consider_decision_trees():
    print("Consider Decision Tree.")
    performances: List[ExperimentResult] = []

    for rnd in range(3):
        for crit in ["entropy", "gini"]:
            for d in range(1, 9):
                params = {
                    "criterion": crit,
                    "max_depth": d,
                    "random_state": rnd,
                }
                f = DecisionTreeClassifier(**params)
                f.fit(X_train, y_train)
                vali_acc = f.score(X_vali, y_vali)
                result = ExperimentResult(vali_acc, params, f)
                performances.append(result)
    return max(performances, key=lambda result: result.vali_acc)


def consider_random_forest():
    print("Consider Random Forest.")
    performances: List[ExperimentResult] = []
    # Random Forest
    for rnd in range(3):
        for crit in ["entropy"]:
            for d in range(4, 9):
                params = {
                    "criterion": crit,
                    "max_depth": d,
                    "random_state": rnd,
                }
                f = RandomForestClassifier(**params)
                f.fit(X_train, y_train)
                vali_acc = f.score(X_vali, y_vali)
                result = ExperimentResult(vali_acc, params, f)
                performances.append(result)
    return max(performances, key=lambda result: result.vali_acc)


def consider_perceptron() -> ExperimentResult:
    print("Consider Perceptron.")
    performances: List[ExperimentResult] = []
    for rnd in range(3):
        params = {
            "random_state": rnd,
            "penalty": None,
            "max_iter": 1000,
        }
        f = Perceptron(**params)
        f.fit(X_train, y_train)
        vali_acc = f.score(X_vali, y_vali)
        result = ExperimentResult(vali_acc, params, f)
        performances.append(result)

    return max(performances, key=lambda result: result.vali_acc)


def consider_logistic_regression() -> ExperimentResult:
    print("Consider Logistic Regression.")
    performances: List[ExperimentResult] = []
    for rnd in range(3):
        for C in [1.0, 0.1, 0.01, 0.001]:
            params = {
                "random_state": rnd,
                "penalty": "l2",
                "max_iter": 100,
                "C": C,
            }
            f = LogisticRegression(**params)
            f.fit(X_train, y_train)
            vali_acc = f.score(X_vali, y_vali)
            result = ExperimentResult(vali_acc, params, f)
            performances.append(result)

    return max(performances, key=lambda result: result.vali_acc)


def consider_neural_net() -> ExperimentResult:
    print("Consider Multi-Layer Perceptron.")
    performances: List[ExperimentResult] = []
    for rnd in range(3):
        params = {
            "hidden_layer_sizes": (32,),
            "random_state": rnd,
            "solver": "lbfgs",
            "max_iter": 500,
            "alpha": 0.0001,
        }
        f = MLPClassifier(**params)
        f.fit(X_train, y_train)
        vali_acc = f.score(X_vali, y_vali)
        result = ExperimentResult(vali_acc, params, f)
        performances.append(result)

    return max(performances, key=lambda result: result.vali_acc)


logit = consider_logistic_regression()
perceptron = consider_perceptron()
dtree = consider_decision_trees()
rforest = consider_random_forest()
mlp = consider_neural_net()

print("Best Logistic Regression", logit)
print("Best Perceptron", perceptron)
print("Best DTree", dtree)
print("Best RForest", rforest)
print("Best MLP", mlp)

#%% Plot Results

# Helper method to make a series of box-plots from a dictionary:
#simple_boxplot(
#    {
#        "Logistic Regression": bootstrap_accuracy(logit.model, X_vali, y_vali),
#        "Perceptron": bootstrap_accuracy(perceptron.model, X_vali, y_vali),
#        "Decision Tree": bootstrap_accuracy(dtree.model, X_vali, y_vali),
#        "RandomForest": bootstrap_accuracy(rforest.model, X_vali, y_vali),
#        "MLP/NN": bootstrap_accuracy(mlp.model, X_vali, y_vali),
#    },
#    title="Validation Accuracy",
#    xlabel="Model",
#    ylabel="Accuracy",
#    save="model-cmp.png",
#)
#
#TODO("1. Understand consider_decision_trees; I have 'tuned' it.")
#TODO("2. Find appropriate max_iter settings to stop warning messages.")
#TODO(
#    "3. Pick a model: {perceptron, logistic regression, neural_network} and optimize it!"
#)

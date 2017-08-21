#!/usr/bin/python3
import numpy as np

corpus = "/home/laboratory/github/homeWork/machineTranslation/data/2000-09-2003.txt.utf8.clean"
train = "/home/laboratory/github/homeWork/machineTranslation/data/train.txt"
test  = "/home/laboratory/github/homeWork/machineTranslation/data/test.txt"

fold = 5
samples = []

with open(corpus, 'r') as f:
    for line in f:
        samples.append(line)
np.random.shuffle(samples)

n = len(samples)
s = n // fold

for i in range(fold):
    train0 = samples[0:i*s]
    testSet   = samples[i*s:(i+1)*s]
    trainSet = samples[(i+1)*s:] + train0
    with open(train + str(i), 'w') as f:
        for trainsample in trainSet:
            f.write(trainsample)
    with open(test + str(i), 'w') as f:
        for testsample in testSet:
            f.write(testsample)


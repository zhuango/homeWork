import random

featurePath = "/home/laboratory/github/data/train/features.txt"
negative = 0.0
positive = 0.0

with open(featurePath, 'r') as f:
    for line in f:
        items = line.strip().split(",")
        if items[-1] == '0':
            negative += 1.0
        else:
            positive += 1.0
    print("positive / negative: " + str( positive / negative))

pos_neg_rate = positive / negative
pos_copy_rate = 0.1 / pos_neg_rate - 1
print("copy rate: " + str(pos_copy_rate))

negative = 0.0
positive = 0.0

sampleFeaturePath = featurePath + ".sample"
with open(featurePath, 'r') as f:
    sample_features = open(sampleFeaturePath, 'w')
    for line in f:
        items = line.strip().split(",")
        sample_features.write(line)
        if items[-1] == '1':
            i = 0
            while i < pos_copy_rate:
                sample_features.write(line)
                positive += 1.0
                i += 1.0
        if items[-1] == '1':
            positive += 1.0
        else:
            negative += 1.0
        
    print("positive / negative: " + str( positive / negative))    
    sample_features.close()
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
neg_drop_rate = 10 * pos_neg_rate
print("drop rate: " + str(neg_drop_rate))

negative = 0.0
positive = 0.0

sampleFeaturePath = featurePath + ".sample"
with open(featurePath, 'r') as f:
    sample_features = open(sampleFeaturePath, 'w')
    for line in f:
        items = line.strip().split(",")
        if items[-1] == '0' and random.uniform(0,1) > neg_drop_rate:
            continue
        sample_features.write(line)
        if items[-1] == '1':
            positive += 1.0
        else:
            negative += 1.0
        
    print("positive / negative: " + str( positive / negative))    
    sample_features.close()
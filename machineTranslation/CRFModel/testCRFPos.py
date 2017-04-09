import numpy as np
from crf import Sample, CRF

with open("../data/label.txt", 'r') as f:
    index = 0
    for line in f:
        Sample.LabelTable[index] = line.strip().split(" ")[0]
        index += 1
with open("/home/laboratory/corpus/cn_vectorTable/cn_vectors_50.txt", 'r') as f:
    for line in f:
        items = line.strip().split(" ")
        Sample.WordsTable[items[0]] = np.array([float(elem) for elem in items[1:]], dtype=np.float)
def load(filename):
    data = []
    with open(filename, 'r') as f:
        for line in f:
            wordSeq = []
            labels  = []
            for items in line.strip().split("  "):
                word_label = items.split("/")
                wordSeq.append(word_label[0])
                labels.append(word_label[0])
            data.append(Sample(wordSeq, labels))
    return data

train = load("/home/laboratory/github/homeWork/machineTranslation/data/train.txt")
test  = load("/home/laboratory/github/homeWork/machineTranslation/data/test.txt")


crf = CRF(50, 52, 35)
crf.SGA(train, iterations=20, a0=19, validate=None)
crf.Sample(test[0])
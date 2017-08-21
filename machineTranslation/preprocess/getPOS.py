#!/usr/bin/python3

filename = "../data/2000-09-2003.txt.utf8"
labelFilename = "../data/pos.txt"
labels = set()

with open(filename, 'r') as f:
    for line in f:
        line = line.strip()
        if line == "":
            continue
        for items in line.split("  "):
            labels.add(items.split("/")[1])

i = 0
with open(labelFilename, 'w') as posStream:
    for label in labels:
        posStream.write(str(i) + " " + str(label) + "\n")
        i+=1
#!/usr/bin/python2
import re
filename = "../data/2000-09-2003.txt.utf8"
recodeFilename = "../data/2000-09-2003.txt.utf8.recode"

newFileStream = open(recodeFilename, 'w')

with open(filename, 'r') as f:
    for line in f:
        lineDecoded = line.decode('utf8')
        lineUtf8    = lineDecoded.encode('utf8').strip()
        if lineUtf8 == "":
            #print("a" + line + "b")
            continue
        lineUtf8 = re.sub('[0-9][0-9]*', 'd', lineUtf8)
        newFileStream.write(lineUtf8 + "\n")

newFileStream.close()
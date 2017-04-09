filename = "../data/199801.txt"
recodeFilename = "../data/199801_utf8.txt"

newFileStream = open(recodeFilename, 'w')

with open(filename, 'r') as f:
    for line in f:
        lineDecoded = line.decode('gbk')
        lineUtf8    = lineDecoded.encode('utf8').strip()
        if lineUtf8 == "":
            print("a" + line + "b")
            continue
        newFileStream.write(lineUtf8 + "\n")

newFileStream.close()
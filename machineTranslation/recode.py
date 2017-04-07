filename = "./199801/199801.txt"
recodeFilename = "./199801/199801_utf8.txt"

newFileStream = open(recodeFilename, 'w')

with open(filename, 'r') as f:
    for line in f:
        lineDecoded = line.decode('gbk')
        lineUtf8    = lineDecoded.encode('utf8')
        newFileStream.write(lineUtf8)

newFileStream.close()
#！/usr/bin/python3
posDict = {}
prf = [0.0, 0.0]
labelmapping = {}
with open("/home/laboratory/github/homeWork/machineTranslation/data/pos.txt",'r') as labelMappingS:
    for line in labelMappingS:
        record = line.strip().split(" ")
        labelmapping[record[0]] = record[1]

with open("/home/laboratory/github/homeWork/machineTranslation/CRFModel/cpp/result1/result8", 'r') as result:
    for line in result:
        result_gold = line.strip().split("\t")
        result = result_gold[0]
        gold   = result_gold[1]
        if gold not in posDict:
            posDict[gold] = [0.0, 0.0, 0.0]
        if result not in posDict:
            posDict[result] = [0.0, 0.0, 0.0]
        posDict[gold][0] += 1
        posDict[result][1] += 1
        if result == gold:
            posDict[gold][2] += 1
            prf[1] += 1
        prf[0] += 1
sortedKey = sorted(posDict, key=lambda k:int(k))
print(sortedKey)
for key in sortedKey:
    pos = posDict[key]
    if pos[0] == 0:
        continue
    r = pos[2] / pos[0]
    try:
        p = pos[2] / pos[1]
    except:
        p = 0
    try:
        f = 2*p*r / (p + r)
    except:
        f = 0.0
    print(labelmapping[key])
    print("count: " + str(pos[0]))
    print("p: {0:.4f}".format(p))
    print("r: {0:.4f}".format(r))
    print("f: {0:.4f}".format(f))
print("total: " + str(prf[1] / prf[0]))
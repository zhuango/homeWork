#！/usr/bin/python3
posDict = {}
prf = [0.0, 0.0, 0.0]
with open("/home/laboratory/github/homeWork/machineTranslation/CRFModel/cpp/result1", 'r') as result:
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
            prf[2] += 1
        prf[0] += 1
        prf[1] += 1
for key in posDict:
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
    print(key)
    print("count: " + str(pos[0]))
    print("p: " + str(p))
    print("r: " + str(r))
    print("f: " + str(f))
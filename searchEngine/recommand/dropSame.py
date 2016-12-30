table = {}
newPredict = open("new_predict_resultGBDT.csv", 'w')
with open("predict_resultGBDT.csv", 'r') as f:
    for line in f:
        if line not in table:
            table[line]= True
for key in table:
    newPredict.write(key)
import numpy as np

import datetime
from sklearn import preprocessing
from sklearn.externals import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn import linear_model
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import make_scorer
from sklearn import datasets
from sklearn.metrics import f1_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
#from sklearn.grid_search import GridSearchCV
from sklearn.metrics import classification_report
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.svm import SVC
from sklearn import tree
from sklearn import svm
from sklearn.ensemble.gradient_boosting import GradientBoostingRegressor

def saveres(filename, uipair, label):
    recPairs = ''
    posenum = 0
    sum = 0
    for p in label:
        if p == 1:
            recPairs += str(int(uipair[sum][0])) + ',' + str(int(uipair[sum][1])) + '\n'  #uid,iid
            posenum += 1
        sum += 1

    neganum = sum - posenum
    percent = (float)(posenum) / neganum
    print 'predict num of pos samples:' + str(posenum) + " ,num of neg examples:" + str(
        neganum) + ",percent of both:" + str(percent)

    fout = open(filename, "w")
    fout.write("user_id,item_id\n" + recPairs)
    fout.close()
#规则1 昨天是否加入购物车
def rule1(uipairs, lastday, feat=[], label=[]):
    conn = MySQLdb.connect(host=sqlhost, user=sqluser, passwd=sqlpswd, db=sqldb, charset='utf8', port=3306)
    cur = conn.cursor()
    sql = "select DISTINCT user_id,item_id from train_user_target_item_new where behavior_type = 3 and date(time) = '" + lastday + "'"
    cur.execute(sql)
    results = cur.fetchall()
    ui_list = uipairs.tolist()

    if len(label) != 0:
        new_uipairs = np.array([])
        new_feat = np.array([])
        new_label = np.array([])
        for row in results:
            uipair = str(row[0]) + ',' + str(row[1])
            if uipair in ui_list:
                i = ui_list.index(uipair)
                new_feat.add(feat[i])
                new_uipairs.add(uipairs[i])
                new_label.add(label[i])

    posnum = len([a for a in new_label if a == 1])  #正样本
    negnum = len(new_label) - posnum
    print 'after rule1 clean,sample posenum is ' + str(posnum) + ' and negnum is ' + str(negnum)

    return new_uipairs, new_feat, new_feat


#最近收藏夹的ui对
def rule2(uipairs, beginday, endday, feat, label):
    conn = MySQLdb.connect(host=sqlhost, user=sqluser, passwd=sqlpswd, db=sqldb, charset='utf8', port=3306)
    cur = conn.cursor()
    sql = "select DISTINCT user_id,item_id from train_user_target_item_new where behavior_type = 3 and date(time) >= '" + beginday + "' and date(time) <= '" + endday + "'"
    cur.execute(sql)
    results = cur.fetchall()
    ui_list = uipairs.tolist()

    new_uipairs = np.array([])
    new_feat = np.array([])
    new_label = np.array([])
    for row in results:
        uipair = str(row[0]) + ',' + str(row[1])
        if uipair in ui_list:
            i = ui_list.index(uipair)
            new_feat.add(feat[i])
            new_uipairs.add(uipairs[i])
            new_label.add(label[i])

    posnum = len([a for a in new_label if a == 1])  #正样本
    negnum = len(new_label) - posnum
    print 'after rule2 clean,sample posenum is ' + str(posnum) + ' and negnum is ' + str(negnum)

    return new_uipairs, new_feat, new_label


#规则2 是否已经购买过
def rule3(uipairs, lastday, feat=0, label=0):
    conn = MySQLdb.connect(host=sqlhost, user=sqluser, passwd=sqlpswd, db=sqldb, charset='utf8', port=3306)
    cur = conn.cursor()
    sql = "select DISTINCT user_id,item_id from train_user_target_item_new where behavior_type = 4 and date(time) = '" + lastday + "'"
    cur.execute(sql)
    results = cur.fetchall()
    rule2 = []

    for row in results:
        uipair = str(row[0]) + ',' + str(row[1])
        rule2.append(uipair)

    for i in range(0, len(uipairs)):
        uipair = str(int(uipairs[i][0])) + ',' + str(int(uipairs[i][1]))
        if uipair in rule2:
            uipairs = np.delete(uipairs, i, 0)
            label = np.delete(label, i, 0)
            feat = np.delete(feat, i, 0)

    posnum = len([a for a in label if a == 1])  #正样本
    negnum = len(label) - posnum
    print 'after rule2 clean,sample posenum is ' + str(posnum) + ' and negnum is ' + str(negnum)


#规则3 没有购买行为,点击行为异常
def rule4(uipairs, feat=0, label=0):
    conn = MySQLdb.connect(host=sqlhost, user=sqluser, passwd=sqlpswd, db=sqldb, charset='utf8', port=3306)
    cur = conn.cursor()
    sql = 'select DISTINCT user_id from train_user_target_item_new where behavior_type = 4'
    cur.execute(sql)
    results = cur.fetchall()
    rule3 = set()

    for row in results:
        rule3.add(row[0])

    for i in range(0, len(uipairs)):
        user_id = int(uipairs[i].splite(',')[0])
        if user_id not in rule3:
            uipairs = np.delete(uipairs, i, 0)
            label = np.delete(label, i, 0)
            feat = np.delete(feat, i, 0)

    posnum = len([a for a in label if a == 1])  #正样本
    negnum = len(label) - posnum
    print 'after rule3 clean,sample posenum is ' + str(posnum) + ' and negnum is ' + str(negnum)


def rulepool4train(uipairs, lastday, feat, label):
    #rule1(uipairs,lastday,feat,label)
    #rule2(uipairs,lastday,feat,label)
    #rule3(uipairs,lastday,feat,label)

    posnum = len([a for a in label if a == 1])  #正样本
    negnum = len(label) - posnum
    print 'after rule pool clean,sample posenum is ' + str(posnum) + ' and negnum is ' + str(negnum)

    return uipairs, feat, label


#规则池
def rulepool4result(uipairs, lastday, probs, threshold):
    uipairs
    cleanedpairs = []
    cleaningpairs = set()
    i = 0
    for prob in probs:
        if prob < threshold:
            cleaningpairs.add(uipairs[i])
        else:
            cleanedpairs.append(uipairs[i])
        i += 1

    rule1(cleaningpairs, lastday)
    rule2(cleaningpairs, lastday)
    rule3(cleaningpairs, lastday)
    cleanedpairs.extend(cleaningpairs)
    return cleanedpairs

def prepare4test(file4feat):
    matrix_file = open(file4feat)
    matrix = np.loadtxt(matrix_file, skiprows=1, delimiter=',')
    row, column = matrix.shape

    train_ui = matrix[:, 0:2]
    train_x = matrix[:, 2:column]
    matrix_file.close()
    print "load " + file4feat + " completed"

    return train_ui, train_x

def prepare4train(file4feat):
    matrix_file = open(file4feat)
    matrix = np.loadtxt(matrix_file, skiprows=1, delimiter=',')
    row, column = matrix.shape

    train_ui = matrix[:, 0:2]
    train_x = matrix[:, 2:column - 1]
    train_y = matrix[:, -1]
    matrix_file.close()
    print "load " + file4feat + " completed"

    return train_ui, train_x, train_y

def train(file4feat):

    uipair, feat, label = prepare4train(file4feat)
    print(label)
    feat = preprocessing.scale(feat)
    np.random.shuffle(feat)#
    #feat = preprocessing.scale(feat)
    estimators = {}
    #estimators['LR'] = linear_model.LogisticRegression(class_weight={1: 25, 0: 1})  #class_weight = {1:1.5,0:1}
    estimators['RF'] = RandomForestClassifier()
    #estimators['GBDT'] = GradientBoostingClassifier()
    #estimators['bayes'] = GaussianNB()
    #estimators['tree'] = tree.DecisionTreeClassifier()
    #estimators['SVM'] = svm.SVC()

    tuned_parameters = {}
    #tuned_parameters['LR'] = [{'C': [1,0.1,0.001],'penalty':['l2','l1'],'class_weight':[{1:25,0:1}, 'auto']}]
    #tuned_parameters['RF'] = [{'n_estimators': [10,100], 'max_depth': [1,3,5,7,9]}]
    #tuned_parameters['GBDT'] = [{'n_estimators': [10,100], 'max_depth': [1,3,5,7,9]}]
    #tuned_parameters['bayes'] = [{'alpha': [1,0,10]}]
    #tuned_parameters['tree'] = [{'max_depth':[1,10,100,1000,None]}]
    #tuned_parameters['SVM'] = [{'kernel': ['rbf'], 'gamma': [1e-3, 1e-4],'C': [1, 10, 100, 1000]},{'kernel': ['linear'], 'C': [1, 10, 100, 1000]}]

    starttime = datetime.datetime.now()
    for k in estimators.keys():
        print("# Tuning hyper-parameters for %s" % k)
        estimators[k].fit(feat, label)
        #label_pred = estimators[k].predict(feat)

    return estimators

def predict(estimators, file4feat):
    uipair, feat = prepare4test(file4feat)
    feat = preprocessing.scale(feat)
    for k in estimators.keys():
        label_pred = estimators[k].predict(feat)
        rulepool4result(uipairs,lastday,probs,0.6)
        saveres('predict_result' + k + '.csv', uipair, label_pred)
        num = len([a for a in label_pred if a == 1]) 
        print 'num of pos samples:' + str(num)

trainData = "/home/laboratory/github/data/train/features.txt.sample"
testData  = "/home/laboratory/github/data/test/features.txt"
estimators = train(trainData)
predict(estimators,testData)

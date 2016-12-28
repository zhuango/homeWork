dataPath = "/home/laboratory/Downloads/dutir_tianchi_mobile_recommend_train_user_train.csv"
import csv
import MySQLdb

conn=MySQLdb.connect(host='localhost',user='root',passwd='lab',db='machineLearning',port=3306)
cur=conn.cursor()

with open('sqls', 'r') as sqlQuery:
    for line in sqlQuery:
        try:
            result = cur.execute(line.strip())
            #conn.commit()
        except MySQLdb.Error,e:
            print "Mysql Error %d: %s" % (e.args[0], e.args[1])
            print(line)

cur.close()
conn.close()

#'119616442', '239814281', '3', '94gn6nd', '4410', '2014-11-26 20:00:00'
# INSERT INTO `dutir_tianchi_mobile_recommend_train_user_train` (`user_id`, `item_id`, `behavior_type`, `user_geohash`, `item_category`, `time`) VALUES ('119616442', '239814281', '3', '94gn6nd', '4410', '2014-11-26 20:00:00');
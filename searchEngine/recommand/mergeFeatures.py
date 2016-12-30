from collections import defaultdict
def ToHash_has_it(filename, delimiter='\t'):
    results = defaultdict(lambda:False)
    with open(filename, 'r') as f:
        for line in f:
            items = line.strip().split(delimiter)
            results[items[0]] = True
    return results

def ToHash_key_string_value_string(filename, keyLength = 1, delimiter='\t', multiKeyConnecter = "_"):
    results = defaultdict(lambda:"0")
    with open(filename, 'r') as f:
        for line in f:
            items = line.strip().split(delimiter)

            key = ""
            i = 0
            while i < keyLength - 1:
                key += items[i] + multiKeyConnecter
                i += 1
            key += items[i]
            
            value = items[i + 1]

            results[key] = value
    return results

folderPath = "/home/laboratory/github/data/train/b"
user_buy            = ToHash_key_string_value_string(folderPath + "user_buy.txt")
user_cart           = ToHash_key_string_value_string(folderPath + "user_cart.txt")
user_click          = ToHash_key_string_value_string(folderPath + "user_click.txt")
user_collect        = ToHash_key_string_value_string(folderPath + "user_collect.txt")
item_buy            = ToHash_key_string_value_string(folderPath + "item_buy.txt")
item_cart           = ToHash_key_string_value_string(folderPath + "item_cart.txt")
item_click          = ToHash_key_string_value_string(folderPath + "item_click.txt")
item_collect        = ToHash_key_string_value_string(folderPath + "item_collect.txt")
user_item_buy       = ToHash_key_string_value_string(folderPath + "u_it_buy.txt", 2)
user_item_cart      = ToHash_key_string_value_string(folderPath + "u_it_cart.txt", 2)
user_item_click     = ToHash_key_string_value_string(folderPath + "u_it_click.txt", 2)
user_item_collect   = ToHash_key_string_value_string(folderPath + "u_it_collect.txt", 2)


user_recent2day_buy             = ToHash_key_string_value_string(folderPath + "user_recent2day_buy.txt")
user_recent2day_cart            = ToHash_key_string_value_string(folderPath + "user_recent2day_cart.txt")
user_recent2day_click           = ToHash_key_string_value_string(folderPath + "user_recent2day_click.txt")
user_recent2day_collect         = ToHash_key_string_value_string(folderPath + "user_recent2day_collect.txt")
item_recent2day_buy             = ToHash_key_string_value_string(folderPath + "item_recent2day_buy.txt")
item_recent2day_cart            = ToHash_key_string_value_string(folderPath + "item_recent2day_cart.txt")
item_recent2day_click           = ToHash_key_string_value_string(folderPath + "item_recent2day_click.txt")
item_recent2day_collect         = ToHash_key_string_value_string(folderPath + "item_recent2day_collect.txt")
user_item_recent2day_buy        = ToHash_key_string_value_string(folderPath + "u_it_recent2day_buy.txt", 2)
user_item_recent2day_cart       = ToHash_key_string_value_string(folderPath + "u_it_recent2day_cart.txt", 2)
user_item_recent2day_click      = ToHash_key_string_value_string(folderPath + "u_it_recent2day_click.txt", 2)
user_item_recent2day_collect    = ToHash_key_string_value_string(folderPath + "u_it_recent2day_collect.txt", 2)

user_item_buy_label             = ToHash_key_string_value_string(folderPath + "17_label.txt", 2)
user_who_buy_thing              = ToHash_has_it(folderPath + "user_which_buy_thing.txt")

featuresPath = "/home/laboratory/github/data/train/features.txt"
features = open(featuresPath, 'w')

user_item_pair = "/home/laboratory/github/data/train/user-item-pairs.txt"
with open(user_item_pair) as f:
    for line in f:
        feature = ""
        user_item = line.strip().split('\t')
        userId = user_item[0]
        itemId = user_item[1]
        userItem = userId + "_" + itemId
        feature += userId + "," + itemId + ","
        # feature += user_buy[userId] + ","
        # feature += user_cart[userId] + ","
        # feature += user_click[userId] + ","
        # feature += user_collect[userId] + ","
        # feature += item_buy[itemId] + ","
        # feature += item_cart[itemId] + ","
        # feature += item_click[itemId] + ","
        # feature += item_collect[itemId] + ","
        # feature += user_item_buy[userItem] + ","
        # feature += user_item_cart[userItem] + ","
        # feature += user_item_click[userItem] + ","
        # feature += user_item_collect[userItem] + ","

        feature += user_recent2day_buy[userId] + ","
        feature += user_recent2day_cart[userId] + ","
        feature += user_recent2day_click[userId] + ","
        feature += user_recent2day_collect[userId] + ","
        feature += item_recent2day_buy[itemId] + ","
        feature += item_recent2day_cart[itemId] + ","
        feature += item_recent2day_click[itemId] + ","
        feature += item_recent2day_collect[itemId] + ","
        feature += user_item_recent2day_buy[userItem] + ","
        feature += user_item_recent2day_cart[userItem] + ","
        feature += user_item_recent2day_click[userItem] + ","
        feature += user_item_recent2day_collect[userItem] + ","

        if not float(user_click[userId]) == 0:
            #interest in item
            feature += str(float(user_item_click[userItem]) / float(user_click[userId])) + ","
            #shopping habit
            feature += str(float(user_buy[userId]) / float(user_click[userId])) + ","
        else:
            feature += "0" + ","
            feature += "0" + ","
        if not float(item_click[itemId]) == 0: 
            #item characteristic
            feature += str( float(item_buy[itemId]) / float(item_click[itemId]) ) + ","
        else:
            feature += "0" + ","
        # user activities
        feature += str( float(user_click[userId]) / float(len(item_click)) ) + ","
        # item popularity
        feature += str( float(item_click[itemId]) / float(len(user_click)) ) + ","
        # buy or not in current day. just for train
        if int(user_item_buy_label[userItem]) > 0:
            feature += "1"
        else:
            feature += "0"
        if user_who_buy_thing[userId]:
            features.write(feature + "\n") 
features.close()
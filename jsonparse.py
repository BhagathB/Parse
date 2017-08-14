import json

source = open("jsonfile","rU")
jsondata = json.load(source)
for items in jsondata['stationBeanList']:
    for x in items:
        print(x + " is :" + str(items[x]) ,end='\n')


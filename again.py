import xml.etree.ElementTree as et

root = et.parse('abc').getroot()
for items in root:
    print(items.get('name'))
    for x in items:
        if(x.tag == 'neighbor'):
            print("{0} is : {1}".format(x.tag, x.get('name')))
        else:
            print("{0} is : {1}".format(x.tag,x.text))
import xml.etree.ElementTree as et

root = et.parse('nxml').getroot()
for sub in root:
    for sub1 in sub:
        print("\n")
        print(sub1.get('classname'))
        for sub2 in sub1:
            print("{0} is : {1}".format(sub2.get('name'),sub2.text))
import xml.etree.ElementTree as et

root = et.parse('contents').getroot()
for tree in root.iter():
    print("{0} is : {1}".format(tree.get('name'),tree.text))
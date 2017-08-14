from xml.etree import ElementTree

with open('contents', 'rt') as f:
    tree = ElementTree.parse(f)

for node in tree.iter('lst'):
    print(node.get('name'))
    for child in node:
        for sub in child:
            name = sub.attrib.get('name')
            value = sub.text
            print(name + " : " + value)


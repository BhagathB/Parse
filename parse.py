import xml.etree.ElementTree as et

root = et.parse('contents').getroot()
for child in root:
    print(child.items(),child.attrib,child.tag,child.get)
    for subchild in child:
        print("{0} is :{1}".format(subchild.get('name'),subchild.text))
        for supersub in subchild:
            print("{0} is :{1}".format(supersub.get('name'), supersub.text))
            for supsup in supersub:
                print("{0} is :{1}".format(supsup.get('name'), supsup.text))
                for supsupsup in supsup:
                    print(supsupsup.text)










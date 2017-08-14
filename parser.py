import xml.etree.ElementTree as ET
tree = ET.parse('abc')
root = tree.getroot()
for country in root.findall('country'):
    rank = country.find('rank').text
    year = country.find('year').text
    gdppc = country.find('gdppc').text
    for neighbor in country.findall('neighbor'):
        neighbors = neighbor.get('name')
        direction = neighbor.get('direction')
    name = country.get('name')
    print(name, rank,year,gdppc,neighbors, direction)
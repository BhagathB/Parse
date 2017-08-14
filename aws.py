import json

source = open("abcd","rU")
parsed_data = json.load(source)
for item in parsed_data:
    print(item['id'])


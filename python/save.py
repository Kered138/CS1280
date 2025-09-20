import json

# file = open('c:/Users/derek/CS1280/python/json/save.json','w+')
# data = { "x": 12153535.232321, "y": 35234531.232322 }
# data = "HIII"
# json.dump(data, file)


class Payload(object):
    def __init__(self,data):
        self.data = data

def as_payload(dct):
    return Payload(dct['action'], dct['method'], dct['data'])




try:
    with open('c:/Users/derek/CS1280/python/json/save.json', 'r') as file:
        data = json.loads(file, object_hook = as_payload)
    print("File data =", data)
    
except FileNotFoundError:
    print("Error: The file 'data.json' was not found.")

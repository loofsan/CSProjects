# Search for an element in a dictionary

myDict = {"name": "Lynn", "age": 17, "address": "California"}

def searchDict(dict,value):
    for key in dict:
        if dict[key] == value:
            return key, value
    return "This value doesn't exist."

print(searchDict(myDict, "Lynn"))

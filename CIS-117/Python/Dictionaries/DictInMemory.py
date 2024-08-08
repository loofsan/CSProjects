#Traversing the Dict
engToSp = {"one": "uno","two": "dos", "three": "tres"}

def traverse(dict):
    for key in dict:
        print(key, dict[key])

traverse(engToSp)


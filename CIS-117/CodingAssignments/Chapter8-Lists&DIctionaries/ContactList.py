str_input = input()
name_input = input()
list1  = str_input.split()

dict1 = {}

for elem in list1:
    list2 = elem.split(",")
    dict1[list2[0]] = list2[1]

print(dict1[name_input])
    

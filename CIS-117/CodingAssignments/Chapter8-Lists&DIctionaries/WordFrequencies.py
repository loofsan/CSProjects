str_input = input()
list1 = str_input.split()
list_copy = [elem.lower() for elem in list1]
dict1 = {}

for elem in list_copy:
    if list_copy.count(elem) == 1:
        dict1[elem] = 1
    else:
        dict1[elem] = list_copy.count(elem)

for i in range(len(list1)):
    if list1[i].lower() == list_copy[i]:
        print(f'{list1[i]} {dict1[list_copy[i]]}')
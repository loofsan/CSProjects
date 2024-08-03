names = ['Ryley', 'Edan', 'Reagan', 'Henry', 'Caius', 'Jane', 'Guto', 'Sonya', 'Tyrese', 'Johnny']
index = int(input())

name = ''
try:
    
    print(f"Name: {names[index]}")
    
except IndexError:

    if index < -(len(names)):
        name = names[0]
    elif index > (len(names)-1):
        name = names[len(names)-1]
    print("Exception! list index out of range")
    print(f"The closest name is: {name}")

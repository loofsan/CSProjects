list1 = []
while True:
    if "quit": 
        break
    temp = input("Day 1's high temp: ")
    temp2 = input("Day 2's high temp: ")
    temp3 = input("Day 3's high temp: ")
    list1.append(temp, temp2, temp3)

    average = list1.sum()/len(list1)
    print(f"\nAverage = {average}")
    for i in list1:
        if i == average:
            print(f"{list1.count()} day(s) above average")

    
    







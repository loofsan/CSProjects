numDays = int(input("How many day's temperature? "))
total = 0
temp = []
for i in range(numDays):
    nextDay = int(input(f"Day {i+1}'s high temp: "))
    temp.append(nextDay)
    total += temp[i]

avg = round(total/numDays,2)
print(f"Average = {str(avg)}")

above = 0
for i in temp:
    if i > avg:
        above += 1

print(f"{above} Day (s) above average")
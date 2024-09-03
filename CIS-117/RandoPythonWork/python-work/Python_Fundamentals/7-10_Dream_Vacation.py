poll = {}
name = "What's your name? "
place = "If you could visit one place in the world,"
place += "\nWhere would you like to go? "
stop = "Would you like the program to stop? "
stop += "\n(Say 'yes' or 'no'): "

a = True

while a:
	name1 = input(name)
	place1 = input(place)
	poll[name1] = place1
	flag = input(stop)
	flag = flag.lower()
	if flag == "yes":
		a = False
		break

for a, b in poll.items():
	print(f"{a} would like to go to {b}")




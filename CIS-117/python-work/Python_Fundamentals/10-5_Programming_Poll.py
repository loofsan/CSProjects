file = "programming_poll.txt"
a = True

while a:
	print("To quit program, enter 'quit'")
	b = input("Why do you like programming?: ")

	with open(file, "a") as d:
		d.write(f"{b}\n")

	if b == "quit":
		break

with open("programming_poll.txt") as x:
	l = x.readlines()

for g in l:
	g = g.replace("quit", "")
	print(g.title()) 

with open(file, "w") as f:
	f.write("")

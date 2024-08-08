file = "learning_python.txt"

with open(file) as a:

	for w in a:
		w = w.replace("Python", "C")
		print(f"{w.rstrip()}\n")

with open(file) as b:

	c = b.read()
	c = c.replace("Python", "C")
	print(c)

with open(file) as z:

	d = z.readlines()

for s in d:
	s = s.replace("Python", "C")
	print(s)

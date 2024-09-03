def count_the(filename):
	try: 
		with open(filename, encoding='utf8') as f:
			contents = f.read()
	except(FileNotFoundError, UnicodeDecodeError, LookupError):
		print("Python couldn't analyze the file.")

	t = contents.lower().count("the")
	y = contents.lower().count("the ")

	print(t)
	print(y)

count_the("moby_dick.txt")


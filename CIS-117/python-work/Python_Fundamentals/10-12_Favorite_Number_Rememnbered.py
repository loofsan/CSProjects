import json 
filename = "saved_numbers.json"

try: 
	w = input("What's your favorite number? ")
	w = int(w)

	if w in filename:
		with open(filename) as v:
			n = json.load(v)

		print(f"I know your favorite number! It's {n}")

	else:
		pass

except ValueError: 
	print("Please put in a number.")
else: 
	with open(filename, "a+") as f:
		json.dump(w, f)

with open(filename) as v:
	n = json.load(v)

print(f"I know your favorite number! It's {n}")




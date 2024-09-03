prompt = "\n(Enter 'quit' to exit)"
prompt += "\nWhat is your age: "

a = True

while a:
	message = input(prompt)
	if message == "quit":
		a = False
		print("The function has stopped")
		break
	age = int(message)
	if age < 3:
		print("The ticket is free.")
	elif 3 <= age <= 12:
		print("The ticket is $10.")
	else:
		print("The ticket is $15.")




sandwich_orders = ["Deli", "Subway", "Foot", "Popeyes", 
				   "KFC", "pastrami", "pastrami", "pastrami"]
finished_sandwiches = []

print("\nThe deli has run out of Pastrami")
while "pastrami" in sandwich_orders:
	sandwich_orders.remove("pastrami")
while sandwich_orders:
	for a in sandwich_orders:
		print(f"I made your {a} sandwich.")
		sandwich = sandwich_orders.pop()
		finished_sandwiches.append(sandwich)

for b in finished_sandwiches:
 	print(f"{b} sandwich has been made.")




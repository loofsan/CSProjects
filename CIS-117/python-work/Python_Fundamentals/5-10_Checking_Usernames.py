current_users = ["admin", "Kathy", "Karen", "Becca", "Lin", "Jeremy"]
new_users = ["Catherine", "Johnny", "Takeo", "Lin", "JEREMY"]


#Making sure that usernames in current users are all same
current_users_lower = []

for a in current_users:
	current_users_lower.append(a.lower())

current_users_upper = []

for v in current_users:
	current_users_upper.append(v.upper())

current_users_title = []

for b in current_users:
	current_users_title.append(b.title())

#New username problems
for new_user in new_users:

	if new_user in current_users:
		print(f"This username, {new_user}, is not available")

	elif new_user in current_users_lower:
		print(f"This username, {new_user}, is not available")

	elif new_user in current_users_title:
		print(f"This username, {new_user}, is not available")

	elif new_user in current_users_upper:
		print(f"This username, {new_user}, is not available")

	else:
		print(f"This username, {new_user}, is available")
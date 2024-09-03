def make_album(name, title):
	music_album = {"Artist Name": name, "Album Title": title}
	return music_album

while True:
	print("If you would like to quit function, enter: quit\n")
	name = input("Insert Artist Name: ")
	if name == "quit":
		break
	title = input("Insert Album Title: ")
	if title == "quit":
		break

	def make_album(name, title):
		music_album = {"Artist Name": name, "Album Title": title}
		return music_album
	print(f"{make_album(name, title)}\n")


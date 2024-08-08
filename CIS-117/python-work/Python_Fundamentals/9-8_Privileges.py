class User:
	def __init__(self, a, b, c):
		self.first_name = a
		self.last_name = b
		self.food = c
		self.login_attempts = 0

	def describe_user(self):
		print(f"The user's name is {self.first_name} {self.last_name}\nThey like to eat {self.food}." )

	def greet_user(self):
		print(f"Nice to meet you, {self.first_name} {self.last_name}")

	def increment_login_attempts(self, attempts = 1):
		self.login_attempts += attempts

	def reset_login_attempts(self):
		self.login_attempts = 0

class Privileges:
	def __init__(self):
		self.privileges =  ["can add post", "can delete post", "can ban user"]
	
	def show_privileges(self):
		for a in self.privileges:
			print(f"They can {a.title()}.")

class Admin(User):

	def __init__(self, a, b, c):
		super().__init__(a, b, c)
		self.privileges = Privileges()

	def describe_user(self):
		print(f"The admin's name is {self.first_name} {self.last_name}\nThey like to eat {self.food}." )



x = input("Insert your first name here: ")
h = input("Insert your last name here: ")
m = input("What do you want to eat right now: ")
x = x.title()
h = h.title()
m = m.lower()

user1 = User(x, h, m)

user1.describe_user()
user1.greet_user()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
print(f"User login attempts = {user1.login_attempts}")
user1.reset_login_attempts()
print(f"Login Attempts Resetted...{user1.login_attempts}")

user2 = Admin("L", "Lawliet", "Sweets")
user2.describe_user()
user2.privileges.show_privileges()




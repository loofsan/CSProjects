class Pet:
    def __init__(self):
        self.name = ''
        self.age = 0
    
    def print_info(self):
        print(f'Pet Information:')
        print(f'   Name: { self.name }')
        print(f'   Age: { self.age }')

class Cat(Pet):
    def __init__(self):
        Pet.__init__(self) 
        self.breed = ''

my_pet = Pet()
my_cat = Cat()

pet_name = input()
pet_age = int(input())
cat_name = input()
cat_age = int(input())
cat_breed = input()

# TODO: Create generic pet (using pet_name, pet_age) and then call print_info()
pet1 = Pet()
pet1.name = pet_name
pet1.age = pet_age
pet1.print_info()
# TODO: Create cat pet (using cat_name, cat_age, cat_breed) and then call print_info()
pet2 = Cat()
pet2.name = cat_name
pet2.age = cat_age
pet2.breed = cat_breed
pet2.print_info()
# TODO: Use my_cat.breed to output the breed of the cat
print(f'   Breed: { pet2.breed }')

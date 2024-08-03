class VendingMachine:
    def __init__(self):
        self.bottles = 20
        
    def purchase(self, amount):
        self.bottles = self.bottles - amount
      
    def restock(self, amount):
        self.bottles = self.bottles + amount
    
    def get_inventory(self):
        return self.bottles
        
    def report(self):
        print(f'Inventory: {self.bottles} bottles')

if __name__ == "__main__":
    # TODO: Create VendingMachine object
    vm = VendingMachine()
    # TODO: Purchase first input number of bottles of drinks
    vm.purchase(int(input()))
    # TODO: Restock second input number of bottles of drinks
    vm.restock(int(input()))
    # TODO: Purchase last input number of bottles of drinks
    vm.purchase(int(input()))
    # TODO: Report inventory
    vm.report()
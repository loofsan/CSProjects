class Plant:
    def __init__(self, plant_name, plant_cost):
        self.plant_name = plant_name
        self.plant_cost = plant_cost

    def print_info(self):
        print(f'   Plant name: {self.plant_name}')
        print(f'   Cost: {self.plant_cost}')


class Flower(Plant):
    def __init__(self, plant_name, plant_cost, is_annual, color_of_flowers):
        super().__init__(plant_name, plant_cost)
        self.is_annual = is_annual
        self.color_of_flowers = color_of_flowers

    def print_info(self):
        super().print_info()
        print(f'   Annual: {str(self.is_annual).lower()}')
        print(f'   Color of flowers: {self.color_of_flowers}')


def print_list(plants):
    for idx, plant in enumerate(plants, start=1):
        print(f'Plant {idx} Information:')
        plant.print_info()
        print()


if __name__ == "__main__":
    my_garden = []

    user_string = input()

    while user_string != '-1':
        parts = user_string.split()
        if parts[0] == 'plant':
            plant_name = parts[1]
            plant_cost = int(parts[2])
            plant = Plant(plant_name, plant_cost)
            my_garden.append(plant)
        elif parts[0] == 'flower':
            plant_name = parts[1]
            plant_cost = int(parts[2])
            is_annual = parts[3] == 'true'
            color_of_flowers = parts[4]
            flower = Flower(plant_name, plant_cost, is_annual, color_of_flowers)
            my_garden.append(flower)

        user_string = input()

    print_list(my_garden)
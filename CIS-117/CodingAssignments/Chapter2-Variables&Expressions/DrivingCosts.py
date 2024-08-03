gas_mileage = float(input())
gas_cost = float(input())

gasCostFor20 = 20 / gas_mileage * gas_cost
gasCostFor75 = 75 / gas_mileage * gas_cost
gasCostFor500 = 500 / gas_mileage * gas_cost

print(f'{gasCostFor20:.2f} {gasCostFor75:.2f} {gasCostFor500:.2f}')
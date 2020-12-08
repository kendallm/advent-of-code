def calculate_fuel_requirement(mass):
    return mass / 3  - 2

if __name__ == "__main__":
    sum = 0
    with open("../input/input_1.txt") as f:
        for line in f:
            fuel = calculate_fuel_requirement(int(line))
            while(fuel > 0):
                sum = sum + fuel
                fuel = calculate_fuel_requirement(fuel)
    print(sum)
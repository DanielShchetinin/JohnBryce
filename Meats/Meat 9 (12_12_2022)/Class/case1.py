
class Car:
    def __init__(self, man: str, mod: str, col, year,
                 fuel_consumption, tank_capacity):
        self.manufacturer = man
        self.model = mod
        self.color = col
        self.year = year
        # liters per 100 km
        self.fuel_consumption = fuel_consumption
        self.tank_capacity = tank_capacity

        self.km = 0
        self.fuel = 0

    def __str__(self):
        return f"{self.manufacturer} {self.model} {self.color}"

    def fill_tank(self, liters) -> bool:
        if 0 < liters <= self.tank_capacity - self.fuel:
            self.fuel += liters
            return True
        return False

    def drive(self, km) -> bool:
        if km > 0 and (self.fuel * (100/self.fuel_consumption)) >= km:
            self.km += km
            self.fuel -= (self.fuel_consumption/100) * km
            return True
        return False


car_mazda = Car('Mazda', '3', 'white', 2015, 20, 50)
ret_val = car_mazda.drive(100)
print(ret_val)
car_mazda.fill_tank(10)
ret_val = car_mazda.drive(15)
print(ret_val)
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def chai_brand(self):
        return self.brand + "!"

    def full_name(self):
        return f"{self.brand} {self.model}"


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size


# create object
my_tesla = ElectricCar("Tesla", "Model S", "85kWh")
print(my_tesla.chai_brand())      # Tesla!
print(my_tesla.full_name())       # Tesla Model S
print(my_tesla.battery_size)      # 85kWh

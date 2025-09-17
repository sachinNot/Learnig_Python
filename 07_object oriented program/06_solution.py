class Car:
    total_car=0

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        Car.total_car+=1

    def get_brand(self):
        return self._brand + "!"
    
    def full_name(self):
        return f"{self.brand} {self.model}"
    
    def fuel_type(self):
        return"petrol or diesel"
    @staticmethod
    def general_description():
        return" Cars are means of transort"
class ElectricCar(Car):
      def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

def fuel_type(self):
    return"Electric charger"
      
my_car=Car("Tata","safari")
Car("Tata","nexon")

print(my_car.general_description())
print(Car.general_description())

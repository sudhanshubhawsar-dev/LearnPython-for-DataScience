class Car:
    def __init__(self,brand,model):
        self.__brand = brand
        self.model = model
    def full_name(self):
        return f"{self.brand}"" "f"{self.model}"
    def get_brand(self):
        return self.__brand
    def set_brand(self,new_brand):
        self.__brand = new_brand
    def fuel_type(self):
        return "Petrol & Diesel"

class ElectricCar(Car):
    def __init__(self, brand, model,battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
    def fuel_type(self):
        return "Electric Charge"
my_electric_car = ElectricCar("tesla","model e","1000kwh")
my_car = Car("maruti","suzuki")


my_car.set_brand("mode new")

print(my_car.fuel_type())
print(my_electric_car.fuel_type())


#1. Create a Python class called 'Circle' with a method to compute its area.
class Circle:
    def __init__(self,radius):
        self.radius = radius
        self.pi = 3.14
    def area_of_circle(self):
        return self.pi * self.radius * self.radius

aoc = Circle(2)
print(aoc.area_of_circle())

class Car:
    def __init__(self, model, year, color):
        self.model = model
        self.year = year
        self.color = color
        self.speed = 0

    def describe_car(self):
        return f' {self.model} , {self.year}, {self.color}, {self.speed}';
    
    def accelerate(self, speed_increase):
        self.speed += speed_increase
        if self.speed > 200:
            self.speed = 200
            return f'Maximum speed reached.';
        else:
            return f'Speed increased to {self.speed}.';
        
    
    def brake(self, speed_decrease):
        self.speed -= speed_decrease
        if self.speed < 0:
            self.speed = 0
            return f'Speed reduced to {self.speed}.';
        else:
            return f'Speed decreased to {self.speed}.';
    

class Electric(Car):
    def __init__(self, model, year, color, battery_capacity=75):
        super().__init__(model, year, color)
        self.battery_capacity = battery_capacity;
    
    def charge_battery(self, charge_amount):
        if charge_amount > 100:
            charge_amount = 100
        self.battery_capacity += charge_amount
        return f'Battery charged to {self.battery_capacity}%.';
    
    def describe_car(self):
        return f'Electric {super().describe_car()}, Battery: {self.battery_capacity}%.';
    


# Test the classes

my_car = Car('Toyota Camry', 2020, 'Red')
print(my_car.describe_car())  # Output: Toyota Camry , 2020, Red, 0

my_car.accelerate(100)
print(my_car.describe_car())  # Output: Toyota Camry , 2020, Red, 100

my_car.brake(50)

my_electric_car = Electric('Tesla Model S', 2021, 'Blue', 80)

print(my_electric_car.describe_car())  # Output: Electric Toyota Camry , 2020, Red, 80

my_electric_car.charge_battery(50)

print(my_electric_car.describe_car())  # Output: Electric Toyota Camry , 2020, Red, 130

print(my_electric_car.brake(20))

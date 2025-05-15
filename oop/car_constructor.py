
class Car:
    model = 2023
    color = "Red"
    price = 200000

    def __init__(self, model, color, price):
        self.model = model
        self.color = color
        self.price = price
        print("Hello Constructor")
    
    def display_info(self):
        print(f"Model: {self.model}")
        print(f"Color: {self.color}")
        print(f"Price: {self.price}")
        print("--------------------")
    
    def set_color(self, new_color):
        self.color = new_color
        print(f"Color updated to: {self.color}")
    
    def get_price(self):
        return self.price
    
    def discount_price(self, discount_percentage):
        discounted_price = self.price - (self.price * (discount_percentage / 100))
        return discounted_price

# Create an instance of Car class

car1 = Car(2023, "Red", 200000)
car1.display_info()

# Update color

car1.set_color("Blue")

# Get price

print(f"Price after discount: {car1.discount_price(10)}")

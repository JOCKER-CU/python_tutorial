class Car:
    def __init__(self, speed=100, model="2020", color="Black"):  # Default values added
        self.speed = speed
        self.model = model
        self.color = color

    def __str__(self):
        return "Speed: " + str(self.speed) + " Model: " + self.model + " Color: " + self.color

    def display(self):
        print("Speed: ", self.speed)
        print("Model: ", self.model)
        print("Color: ", self.color)


# Example usage
car1 = Car(200, "2021", "Red")
car1.display()

car2 = Car(150, "2019", "Blue")
car2.display()

car1.speed = 250
car1.display()

# car3 without parameters, using default values
car3 = Car()
car3.display()

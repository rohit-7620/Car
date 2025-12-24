class Car:
    def __init__(self, brand, model, color):
        # Attributes (Data)
        self.brand = brand
        self.model = model
        self.color = color
        self.speed = 0  # Initial speed is 0

    def accelerate(self, amount):
        """Increase the speed of the car."""
        self.speed += amount
        print(f"The {self.brand} accelerated. Current speed: {self.speed} km/h")

    def brake(self):
        """Stop the car."""
        self.speed = 0
        print(f"The {self.brand} has stopped.")

# --- Using the Code ---

# 1. Create an "Object" (an instance of the class)
my_car = Car("Tesla", "Model 3", "Red")

# 2. Access attributes
print(f"I own a {my_car.color} {my_car.brand} {my_car.model}.")

# 3. Call methods
my_car.accelerate(50)
my_car.brake()

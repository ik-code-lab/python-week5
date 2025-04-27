class Vehicle:
    
    def __init__(self, name):
        
        self.name = name

    def move(self):
        
        print(f"{self.name} is moving.")

class Car(Vehicle):
    
    def move(self):
        
        print(f"{self.name} is Driving")

class Plane(Vehicle):
    
    def move(self):
        
        print(f"{self.name} is Flying")

class Boat(Vehicle):
    
    def move(self):
        
        print(f"{self.name} is Sailing")

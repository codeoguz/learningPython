#Car class
class Car:
    def __init__(self, price, passengers, tires = 4) -> None:
        self.price = price
        self.tires = tires
        self.passengers = passengers

class Ranger(Car):
    def __init__(self, price, tires, passengers, warranty) -> None:
        super().__init__(price, tires, passengers)
        self.warranty = warranty
    
        
myCar = Ranger(500, 6, 8, 'Levent Warranty Service')

print(myCar.passengers, myCar.price, myCar.tires, myCar.warranty)


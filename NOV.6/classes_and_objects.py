
#Object orientated Programming (OOP)
#Technique of using classes to model real world things
#A class is a blueprint to create/instantiate objects from 
#Each object will have it's own copy of attributes and methods from the class
class Car:
    #constructor method
    #a method called __init__ that executes when you instantiate an object
    # self refers to the object using this method
    def __init__(self, make, model, year, speed):
        self.make = make
        self.model = model
        self.year = year
        self._speed = 0
    
    # Methods provide behaviour for an object
    def Honk(self):
        print(f'{self.make}, {self.model} says Beep Beep!')

    def Accelerate(self, amount):
        self._speed += amount
    
def main():
    #instantiate a new car called car1
    car1 = Car('Ford','F150',2020,0)
    car2 = Car('Mazda','3',2017,0)
    car3 = Car('Mercedes','SmartCar',2010,0)
    
    print(car1.model)
    print(car2.model)
    print(car3.model)
    
    #change attribute values
    car2.model = 6
    print(car2.model)

    #in Python you can add sttrubutes to objects
    car3.seats = 2
    print(car3.seats)
    
    #Test a method
    car1.Honk()
    car2.Honk()
    
    #accelerate
    print(f'Current speed: {car1._speed}')
    car1.Accelerate(40)
    print(f'Current speed: {car1._speed}')
    car1.Accelerate(100)
    print(f'Current speed: {car1._speed}')


if __name__=='__main__':
    main()


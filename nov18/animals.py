# create an Animal class with name, color, num_legs attributes
#code the constructor

class Animal:
    def __init__(self, name:str, color:str, num_legs:int)->None:
        self.name = name
        self.color = color
        self.num_legs = num_legs
    #override __str__ to return:
    
    def __str__(self)->str:
        return (f"Name: {self.name}\n" 
               f"Color: {self.color}\n"
               f"Number of Legs: {self.num_legs}"
        )
    def eat(self)->None:
        print(f"{self.name} starts eating. Yum Yum!")
    
    def make_a_noise(self)->None:
        print(f"{self.name} makes an interesting noise....")
        
    def move(self)->None:
        print(f"{self.name} moves around")
        
        
#Dog class which inherits from animal
class Dog(Animal):
    def __init__(self, name:str, color:str, num_legs:int, breed:str)->None:
        #super() refers to the Parent class(Animal)
        #call the constructor from the Parent(Animal)
        super().__init__(name, color, num_legs)
        self.breed = breed
    #override the __str__ from the parent(Animal) to include breed
    def __str__(self)->str:
        return_string = super().__str__()
        return_string += f"Breed: {self.breed}\n"
        return return_string

#Testing
animal1 = Animal("Patrick", "Blue", 2)
print(animal1)
animal1.eat()
animal1.make_a_noise()
animal1.move()
dog1 = Dog("Judas", "lime green", 4, "labrador")
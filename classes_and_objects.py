#Object oriented programming (OOP)
#We create classes that model real world things/concepts

#A class is like a blueprint
#We make objects from the class

#classes can contain:
    #attributes - describe the class
    #methods - perform a task.

#blueprint for a car object
class Car:

    #a function in a class is called a method
    #__init__ is a method that runs when you create an object
    #self must be in every method parameter list and the first parameter
    #self referes to the current object being created
    #when we create an object we instantiate an object
    def __init__(self, make: str, model: str, year: int)-> None:
        self.make = make
        self.model = model
        self.year = year
        #initialize speed to 0 for a new car object
        #rename attribute to _speed to indicate it should not be set directly
        self._speed = 0

    #Methods - provide behaviour(verb based) actions for an object
    def Honk(self)-> None:
        print(f'{self.make}, {self.model} says Beep Beep!')
    def Accelerate(self,amount):
        self._speed += amount

    #override the __str__ method to print the objects attribute values instead of the objects memory location
    def __str__ (self)-> str:
        return f"{self.make}, {self.model}, {self.year}, {self._speed}"
    
    # __repr__ is used for testing and debugging. It usually returns code to create the object
    def __repr__(self) -> str:
        return f'Car({self.make},{self.model},{self.year})'
    

    

def main():
    #Create(instantiate) a new car object from the Car class called car1
    car1 = Car('Ford','F150',2020)
    #Create(instantiate) a new car object from the Car class called car2
    car2 = Car('Mazda','3',2017)
    

    #access the attributes of an object
    print(f"{car1.make}, {car1.model}")
    #change an attribute
    car1.model = 'F350'
    print(f"{car1.make}, {car1.model}")

    #user defined car object
    make = input('Enter the make: ')
    model = input('Enter the model: ')
    year = int(input('Enter the year: '))
    #instantiate a new car3 from the user input
    car3 = Car(make, model, year)  

    #python allows you to add attributes to an object
    car3.seats = 5
    print(f'{car3.make}, {car3.seats}')

    #Honk car1 horn
    #car1 reference is passed into the self parameter of the honk method
    car1.Honk()
    car2.Honk()

    print (f'{car1._speed} km/h')
    car1.Accelerate(40)
    print (f'{car1._speed} km/h')
    car1.Accelerate(60)
    print (f'{car1._speed} km/h')

    print (f'{car2._speed} km/h')

    #what happens when you print an object
    print(car1)#prints the memory location. Not useful
    #when you print an object it calls __str__
    print(f'Here is some info about car1: {car1}')
    #much faster than
    print(f'Here is some info about car1:{car1.make}, {car1.model}, {car1.year}, {car1._speed}')
    #to test the __repr__ override:
    print([car1])
if __name__ == '__main__':
    main()






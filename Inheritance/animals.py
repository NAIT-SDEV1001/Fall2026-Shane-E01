#create a class called Animal with name, color, num_legs attributes
class Animal:
    def __init__(self, name:str,color:str,num_legs:int)->None:
        self.name = name
        self.color = color
        self.num_legs = num_legs

    def __str__(self)->str:
        return (f"Name: {self.name}\n"
                f"Color: {self.color}\n"
                f"Number of Legs: {self.num_legs}\n"
        )

    def __repr__(self)->str:
        #!r places quotes around the string
        return f"Animal(name = {self.name!r},color = {self.color!r},num_leg = {self.num_legs})"

    #create a method called eat() that prints an eat message which includes the name of the animal
    def eat(self)->None:
        print(f"{self.name} starts eating. Yum Yum!")

    def make_a_noise(self)->None:
        print(f"{self.name} makes an interesting noise")

    def move(self)->None:
        print(f"{self.name} moves around")    


#inherit from Animal
class Dog(Animal):
    def __init__(self, name:str, color:str, num_legs:int, breed:str)->None:
        #pass the constructor values into the parent class(Animal) constructor
        # super() refers to the parent class (Animal)
        super().__init__(name,color,num_legs)
        self.breed = breed

    #add breed to the return string for __str__
    def __str__(self)->str:
        #get the return string from the parent __str__()
        return_string = super().__str__()
        #add (string concatonation) the additional string for a dog
        return_string += f"Breed: {self.breed}\n"
        return return_string

    def chase_car(self)->None:
        print(f"{self.name} chases a car!")
    #override the parent class make_a_noise() for dog objects
    def make_a_noise(self)->None:
            print(f"{self.name} goes Woof Woof")    


def main():
    animal1 = Animal("Buddy","white",2)

    dog1 = Dog("Scooby Doo","brown",4,"Great Dane") 
    print (dog1.name)
    print(dog1)
    dog1.chase_car()
    dog1.eat()
    dog1.move()
    animal1.make_a_noise()
    dog1.make_a_noise()

if __name__ == "__main__":
    main()



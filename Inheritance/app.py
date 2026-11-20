from animals import Animal,Dog, Cat, Bird

def main():
    dog = Dog("Boots","Black and White",4,"Schnoodle")
    cat = Cat("Meow","White",4,"solid",10)
    bird = Bird("Tweety","Green",2,20)

    #create a list of the animals
    animals = [dog, cat, bird]

    #loop through the list, print out the name, color and number of legs for each animal and have each animal make a noise, move, and eat. 

    for animal in animals:
        print("---------")
        print(animal)
        animal.make_a_noise()
        animal.move()
        animal.eat()
        #ONLY call the chase_car() if that animal is a dog
        #if animal variable is holding a Dog object
        if isinstance(animal,Dog):
            animal.chase_car()
        if isinstance(animal,Cat):
            animal.knock_things_off_ledge()

if __name__ == "__main__":
    main()



# -------------
# Name: Boots
# Color: Black and White
# Number of Legs: 4

# Boots makes an interesting noise
# Boots runs around
# Boots starts eating. Yum Yum!
# -------------
# Name: Meow
# Color: White
# Number of Legs: 4

# Meow makes an interesting noise
# Meow runs around
# Meow starts eating. Yum Yum!
# -------------
# Name: Tweety
# Color: Green
# Number of Legs: 2

# Tweety makes an interesting noise
# Tweety runs around
# Tweety starts eating. Yum Yum!
    





if __name__ == "-__main__":
    main()

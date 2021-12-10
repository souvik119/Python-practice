# there may be attributes that will be same for all instances of the class
# example in Dog class all dogs are mammals so that could be a class object

# methods are functions defined within the body of the class to perform operations on attributes

class Dog():
    #class object attributre defined here
    #same for all instances of the class
    #no need for self keyword as it refers to specific instance
    species = 'mammal'

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    #operations/actions that work with objects in some way
    def bark(self, number):
        print(f'WOOF! my name is {self.name} and the number is {number}')

my_dog = Dog(name='Rocky', breed='Lab')

print(my_dog.breed)
print(my_dog.name)
print(my_dog.species) #even though not defined in constructor still available

#calling method
my_dog.bark(10)


class Circle():
    #class attribute
    pi = 3.14
    #this can be accessed as :
    # Circle.pi - this is preferred as makes it more obvious
    # self.pi

    def __init__(self, radius=1):
        self.radius = radius

    def get_circumference(self):
        return 2 * Circle.pi * self.radius

    def get_area(self):
        return Circle.pi * (self.radius ** 2)

my_circle = Circle()
print(my_circle.get_area())
print(my_circle.get_circumference())
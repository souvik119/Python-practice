# Inheritance : using classes that have already been defined
# reuse code and reduce complexity

#base class
# class Animal():
#     def __init__(self):
#         print("Animal Created")

#     def who_am_i(self):
#         print("I am an animal")

#     def eat(self):
#         print("I am eating")

# #derived class
# class Dog(Animal):
#     def __init__(self):
#         Animal.__init__(self)
#         print("Dog created")
    
#     #override base class method
#     def who_am_i(self):
#         print("I am a dog")

#     #can also add on methods
#     def bark(self):
#         print("WOOF!")


# mydog = Dog()
# #can access base class's methods
# mydog.eat()
# mydog.who_am_i()
# mydog.bark()

# Plymorphism : different object classes can share the same method name

class Dog():
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + " says woof!"

class Cat():
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + " says meow!"

niko = Dog("niko")
felix = Cat("felix")

print(niko.speak())
print(felix.speak())

# here speak is the same method name in both the classes but methods are executed according to the object
for pet in [niko, felix]:
    print(type(pet))
    print(type(pet.speak()))


def pet_speak(pet):
    print(pet.speak())

pet_speak(niko)
pet_speak(felix)

#Abstract class - only inteded to be base class without ever expecting to have objects created

#abstract class
class Animal():
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implment this abstract method")

# If we create an instance of Animal
myanimal = Animal("fred")
myanimal.speak() 
#will get an error since we do not expect an instance of Animal class to be created and access 
# this abstract method from base class
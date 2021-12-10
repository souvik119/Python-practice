# OOP allows programmers to create their own objects that have methods and attributes
# name of class usually camel casing
# example class NameOfClass():
# self keyword to connect method/attribute to the class

# class Dog():
#     def __init__(self, breed): #constructor
#         self.breed = breed #this is an attribute

# #create instance of Sample class
# # my_sample = Sample()
# # print(type(my_sample)) #this shows my_sample is an object of type Sample

# my_dog = Dog(breed = 'Lab')
# print(my_dog.breed)

class Dog():
    def __init__(self, breed, name, spots):
        self.breed = breed #string
        self.name = name #string
        self.spots = spots #boolean


my_dog = Dog(breed='Lab', name='Rocky', spots=False)

print(my_dog.breed)
print(my_dog.name)
print(my_dog.spots)
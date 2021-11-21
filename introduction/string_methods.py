# Immutability property
# means we cannot change the string once defined

name = "Souvik"
#name[0] = 'P' this will throw an error as this is not allowed in python
# If we want to create Pouvik from Souvik we can do it as follows with concatenation
new_name = 'P' + name[1:]
print(new_name)

#another example of string concatenation
x = "Hello World"
x = x + ", it is beautiful out there"
print(x)

#using multiplication of string
letter = 'z'
print(letter * 10)

x = "Hello World"
print(x.upper())
print(x.lower())
print(x.split())
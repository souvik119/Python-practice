mystring = "Hello World"
print(mystring[0])
#to get character r
print(mystring[8])

#to get l of world 2 ways 
#print(mystring[9])
print(mystring[-2])

mystring = "abcdefghijk"
print(mystring)
#get everything from c to the end
print(mystring[2:])
#get just abc
print(mystring[:3]) #end index is not included

#get def
print(mystring[3:6])

#get bc
print(mystring[1:3])

#grab the whole string
print(mystring[:])

#go from start to end and include every 2nd character
print(mystring[::2])

#use start stop and step together
print(mystring[2:8:3])

#clever way to reverse a string
print(mystring[::-1])
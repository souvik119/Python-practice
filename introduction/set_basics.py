#unordered collection of unique elements
#there can only be one representative of the same object

myset = set()
myset.add(1)
print(myset)

myset.add(2)
print(myset)

#even thoufh its was addeed twice 2 will only show up once
myset.add(2)
print(myset)

mylist = [1,1,1,1,2,2,2,2,2,3,3,3,3,3,3,3]
print(set(mylist))
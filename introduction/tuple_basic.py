# tuple very similar to lists, they have one difference - immutability
# once an element is inside a tuple , cannot be reassigned
t = (1, 2, 3)
mylist = [1, 2, 3]

print(type(t))
print(type(mylist))

print(len(t))

t = ('a', 'a', 'b')

print(t.count('a'))
print(t.index('a'))

#t[0] = 'x' this will result in an error since tuple is immutable

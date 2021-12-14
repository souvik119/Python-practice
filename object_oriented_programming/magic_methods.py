mylist = [1, 2, 3]
print(len(mylist))

# what if we try to use len on one of objects created by us
# typeerror same for print() or any such built in functions

# own user defined objects to use special build in methods -> magic/dunder methods

class Book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    #this is for print() function that uses string representation
    def __str__(self):
        return f'{self.title} by {self.author}'

    #this is for using len()
    def __len__(self):
        return self.pages

    #this is for deleting
    def __del__(self):
        print('A book object has been deleted')


b = Book('Python is awesome', 'Souvik', 200)
print(b) #uses __str__ method return
print(len(b)) #in this case number of pages retured
del b

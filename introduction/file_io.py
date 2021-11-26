#have to use full paths since cwd is one level up i.e., C:\\Users\\sghosh\\Documents\\Python-practice

myfile = open('C:\\Users\\sghosh\\Documents\\Python-practice\\introduction\\myfile.txt')
print(myfile.read())
#if we want to read the same file again must go back to start of the file
myfile.seek(0)
print(myfile.read())

myfile.seek(0)
print(myfile.readlines())

myfile.close()

#better way of opening file
with open('C:\\Users\\sghosh\\Documents\\Python-practice\\introduction\\myfile.txt') as my_new_file:
    contents = my_new_file.read()

print(contents)

with open('C:\\Users\\sghosh\\Documents\\Python-practice\\introduction\\myfile.txt', mode='a') as myfile:
    myfile.write('\nthis is the fourth line')
# os and shutil modules allow us to easily navigate files and directories on the computer 
# and perform actions on them such as moving or deleting

import os
import shutil #shell utilities module


# print(os.getcwd())
# print(os.listdir('C:\\Users'))

# shutil.move('practice.txt', 'C:\\Users\\sghosh\\Documents')

# three ways of deleting a file
# os.unlink(path) - deletes a file at the path provided
# os.rmdir(path) - deletes a folder(must be empty)
# os.rmtree(path) - PERMANENTLY deletes files and folders at the specified location. This cannot be reversed
# safer alternative to rmtree is send2trash (pip install send2trash)


# os.walk - generates directory tree rooted at the top
path = 'C:\\Users\\sghosh\\Documents\\Python-practice'
for folder, sub_folders, files in os.walk(path):
    print(f'Currently looking at folder : {folder}')
    print('\tSubfolders in this folder:')
    for sub_folder in sub_folders:
        print(f'\t\t{sub_folder}')
    print('\tFiles in this folder:')
    for file in files:
        print(f'\t\t{file}')
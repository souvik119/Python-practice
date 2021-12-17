# It is always preferable to craete a virtual environment for each project separately to keep 
# requirements specific to that particular project
# 
# Steps to create and activate virtual environment
# python -m pip install virtualenv  - this will install virtualenv module needed for creating
# python -m virtualenv .env  - Execute it in the folder you want to create virtual env
# .env/Scripts/activate  - this will activate virtual env
# pip install -r requirements.txt  - if there is a requirements.txt document

# After creating and activating virtual environment use pip to install external libraries
# pip install <module name>

# craete your own modules nothing but .py scripts used in other .py scripts
# packages are collection of modules

def my_func():
    print("Hey I am in external_modules.py")
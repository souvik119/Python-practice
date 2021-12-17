# from external_modules import my_func

# my_func()

# Important to have __init__.py (blank file) to make folder/subfolder a package

from MyMainPackage import some_main_script
from MyMainPackage.SubPackage import subscript

some_main_script.report_main()
subscript.sub_report()
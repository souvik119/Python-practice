import pdb
#this helps debug the issues we are encountering

x = [1, 2, 3]
y = 2
z = 3

result_one = y + z
pdb.set_trace() #pause execution and check variable values
result_two = y + x
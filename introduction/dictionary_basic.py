# dictionaries are unordered mappings for storing objects
# key-value pairing

# key value pair allows user to quickly grab objects without needing to know index loaction
# unordered cannnot be sorted

my_dict = {'key1':'value1', 'key2':'value2', 'key3':'value3'}
print(my_dict)

print(my_dict['key2'])

#example price lookup dict in a strore
price_lookup = {'apple':2.99, 'orange':1.99, 'milk':5.80}

#dictionary can also store list/dictionary itself as values
d = {'k1': 123, 'k2':[0,1,2], 'k3':{'insidekey':100}}
print(d['k2'][1])
print(d['k3']['insidekey'])

for k,v in my_dict.items():
    print(k, v)
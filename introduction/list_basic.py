new_list = ['one', 'two', 'three', 'four', 'five', 'six', 'seven']
print(new_list)
#list is mutable meaning it can be modified in place
new_list[0] = 'ONE IN CAPS'
print(new_list)
new_list.append('eight')
print(new_list)
popped = new_list.pop()
print(popped)

#pop can also remove and return item at specific location
popped_item = new_list.pop(0)
print(popped_item)
print(new_list)

example_list = ['q', 'a', 'b', 'i', 'd']
example_list_num = [1, 4, 23, 2, 45, 13]

#sorts in place
example_list.sort()
print(example_list)

#reverse in place
example_list_num.reverse()
print(example_list_num)
def even_check(num):
    return num % 2 == 0

#return True if any number is even inside a list
# def check_even_list(num_list):
#     for num in num_list:
#         if num % 2 == 0:
#             return True
#         else:
#             pass
#     return False # if the whole loop executed that means we covered all the elements

# print(check_even_list([1, 3, 5]))
# print(check_even_list([2, 4, 5]))
# print(check_even_list([1, 5, 10]))
# print(check_even_list([10, 5, 1]))

def check_even_list(num_list):
    # return all the even numbers

    #placeholder varibales
    even_numbers = []
    for num in num_list:
        if num % 2 == 0:
            even_numbers.append(num)
        else:
            pass
    return even_numbers # if the whole loop executed that means we covered all the elements

print(check_even_list([1, 3, 5]))
print(check_even_list([2, 4, 5]))
print(check_even_list([1, 5, 10]))
print(check_even_list([10, 5, 1]))
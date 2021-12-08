# accpeting input from a user
# by default type of the input is str need to conver it explicitly

# result_int = int(input("Enter a number"))
# print(type(result_int))

#validating user input
# def user_input():
#     choice = 'WRONG' #setting initial value to string so that loop runs first time
#     while choice.isdigit() == False:
#         #keep running the loop till user enters a digit
#         choice = input("Please enter a number (0-10): ")
#         if choice.isdigit() == False:
#             print('Please try again! that is not a digit')
#     return int(choice)

# print(user_input())

#adding further validation
#number to be between 0-10

def user_input():
    choice = 'WRONG' #setting initial value to string so that loop runs first time
    acceptable_range = range(0,11)
    in_range = False #initial False flag
    while choice.isdigit() == False or in_range == False:
        #keep running the loop till user enters a digit or number not in range
        choice = input("Please enter a number (0-10): ")
        if choice.isdigit() == False:
            print('Please try again! that is not a digit')
        else:
            if int(choice) in acceptable_range:
                in_range = True
            else:
                print('Sorry number not in range')
    return int(choice)

print(user_input())
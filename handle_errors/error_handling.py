# Errors bound to happen esp when someone else uses your script in an unexpected way
# Currently any error will cause script to stop
# use error handling to let script continue with other code even if there is an error

# 3 keywords for error handling
# try - block of code to be attempted (may lead to an error)
# except - block of code that will execute if there is an error in try block
# finally - block of code to be executed regardless of an error

# try:
#     # WANT TO ATTEMPT THIS CODE
#     # MAY HAVE AN ERROR
#     result = 10 + 10
# except:
#     print('Something happened')
# else:
#     print('Add went well!')
#     print(result)


# try:
#     f = open('testfile', 'r')
#     f.write('Write a test line')
# except TypeError: #for specific error types
#     print('There was a type error')
# except OSError:
#     print('Hey you have an os error')
# finally: #this always runs
#     print('I always run')


def ask_for_int():
    while True:
        try:
            result = int(input('Please provide a number: '))
        except:
            print('Whoops that is not a number')
            continue
        else:
            print('Yes thank you')
            break
        finally:
            print('End of try/except/finally')
            print('I will always run at the end')

ask_for_int()


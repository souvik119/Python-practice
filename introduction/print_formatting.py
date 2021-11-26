# using .format() method
print("This is a string {}".format("INSERTED"))

print("The {} {} {}".format('fox', 'brown', 'quick'))

#to format the above correctly
print("The {2} {1} {0}".format('fox', 'brown', 'quick')) #use index nos as it appears in format

#can repeat indexes
print("The {0} {0} {0}".format('fox', 'brown', 'quick'))

#can use variable names to make it easier
print("The {q} {b} {f}".format(f = 'fox', b = 'brown', q = 'quick'))

#float formatting
result = 100/777
#value:width.precision f
print("The result was {r:1.3f}".format(r = result))

#increasing width value (adding whitespace)
print("The result was {r:10.3f}".format(r = result))
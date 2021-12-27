import re

# character identifiers
# \d - digit
# \w - alphanumeric (also includes _)
# \s - white space
# \D - non digit
# \W - non alphanumeric
# \S - non whitespace


# quantifiers
# + - occurs one or more time
# {3} - occurs exactly 3 times
# {2,4} - occurs 2 to 4 times
# {3,} - occurs 3 or more times
# * - occurs 0 or more times
# ? - occurs once or none example plurals? -> plural (matching if s occurs once or none)

text = 'My phone is 408-555-7777'
# phone = re.search(r'\d\d\d-\d\d\d-\d\d\d\d', text)
# better way
# phone = re.search(r'\d{3}-\d{3}-\d{4}', text)
phone_pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})') # creating groups
results = re.search(phone_pattern, text)

print(results.group())
print(results.group(1)) #not start at 0
print(results.group(2))
print(results.group(3))
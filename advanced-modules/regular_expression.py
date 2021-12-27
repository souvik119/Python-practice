# pattern structure (maybe not have the exact match)
# regex allows us to search for general patterns
# example - user@email.com
# pattern - "text"+"@"+"text"+".com"


# example - phone number
# (555)-555-5555 -> r"(\d\d\d)-\d\d\d-\d\d\d\d" -> r"(\d{3})-\d{3}-\d{4}"

import re

# pattern = 'phone'
# text = "The agent's phone number is 408-555-1234. Call soon!"
# print(re.search(pattern, text)) # match object

# pattern = 'NOT IN TEXT'
# print(re.search(pattern, text))

# pattern = 'phone'
# text = "The agent's phone number is 408-555-1234. Call soon!"
# match = re.search(pattern, text)
# print(match.span())
# print(match.start())
# print(match.end())
# this will only find first match

pattern = 'phone'
text = 'my phone once, my phone twice'
# match = re.findall(pattern, text)
# print(match)
# print(len(match))

for match in re.finditer(pattern, text):
    print(match) # returns match objects
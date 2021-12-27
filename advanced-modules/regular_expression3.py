import re

# additional regex syntax
# wilcards
# . - single char (also whitespace so be careful)
# | - OR
# ^ - starts with
# $ - ends with
# [^] - exclude


print(re.search(r'cat|dog', 'the cat is here'))
print(re.findall(r'.at', 'The cat in the hat'))

print(re.findall(r'^\d', '1 is a number')) #catch a string starting with a digit
print(re.findall(r'\d$', 'number is 2')) #catch a string ending with a digit

phrase = 'there are 3 numbers 34 inside 5 this sentence'
pattern = r'[^\d]+' # exclude digits
print(re.findall(pattern, phrase))

test_phrase = 'This is a string! But it has punctuation. How can we remove it?'
print(re.findall(r'[^!.? ]+', test_phrase)) #exclude !.? symbols

text = 'Only find the hyphen-words in this sen-tence'
pattern = r'[\w]+-[\w]+' # also \w+-\w+ would work but easier to read with []
print(re.findall(pattern, text))
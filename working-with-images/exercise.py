from PIL import Image

words = Image.open('word_matrix.png')
mask = Image.open('mask.png')

#check original images
# mask.show()
# words.show()

# check size of each image
# print(words.size)
# print(mask.size)

mask = mask.resize((1015,559)) # resizing mask to fit words
# print(mask.size)

# increase transparency of the image
mask.putalpha(300)

#paste modified mask image over words image
words.paste(mask, (0,0))

# show final result
words.show()
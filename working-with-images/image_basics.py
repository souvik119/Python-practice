from PIL import Image # even though module name is pillow import from PIL

# mac = Image.open('example.jpg')
# print(type(mac))
# mac.show() # to output the image
# print(mac.size)
# print(mac.filename)
# print(mac.format_description)

# operations
# cropping
# mac.crop((0,0,100,100)).show() # four item tuple as argument left, upper, right, lower pixel coordinates)

# pencils = Image.open('pencils.jpg')
# print(pencils.size)

# # starting coordinates for x and y
# x = 0
# y = 0

# # end point for cropping
# w = 1950/3 # 1/3rd of the image width
# h = 1300/10 # 10% of the image height

# pencils.crop((x,y,w,h)).show()

# COPY AND PASTE CROPPED IMAGE
# computer = mac.crop((x,y,w,h))
# mac.paste(im=computer, box=(0,0))


# RESIZE THE IMAGE
# mac.resize((3000,500))

# ROTATE 90 deg
# mac.rotate(90)
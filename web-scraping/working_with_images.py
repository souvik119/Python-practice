# always check copyright permission before downloading and using a pic
import requests
import bs4

result = requests.get('https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)')
soup = bs4.BeautifulSoup(result.text, 'lxml')
images = soup.select('.thumbimage') # grabbing class thumbimage
computer = images[0]['src']
#get that image
image_link = requests.get('https:'+computer)
f = open('my_test_image.jpg', 'wb') # write binary
f.write(image_link.content)
f.close()
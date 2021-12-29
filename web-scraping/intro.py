# when a browser loads a website, user gets to see the "front-end" of the website -> html, css, javascript

# rules of webscraping:
# try to get permission before scraping
# if you make too many attempts/requests IP could get blocked
# some sites automatically block scraping software

# limitations:
# every site is unique so every script is unique
# slight change/update to a website may completely break your script

import requests
import bs4

#grab the title
result = requests.get('https://example.com/')
# print(type(result))
# print(result.text)
soup = bs4.BeautifulSoup(result.text, 'lxml') # text string and what engine to use
# print(soup)
# print(soup.select('title')) #returns a list of titles with the tag
# print(soup.select('h1'))

# to get just the text
print(soup.select('title')[0].getText())
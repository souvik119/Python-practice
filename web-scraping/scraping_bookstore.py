# this is where we will be iteratively scraping many pages of book listings
# to get the title of only those books with ratings of 2 star

import requests
import bs4

base_url = 'https://books.toscrape.com/catalogue/page-{}.html'
two_star_titles = []

# try this for the first page
# url = base_url.format(1)
# print(url)
# result = requests.get(url)
# soup = bs4.BeautifulSoup(result.text, 'lxml')
# all info about each book is contained in product_pod class
# book_info = soup.select('.product_pod')
# print(book_info)
# print(book_info[0].select('.star-rating.Three')) #have to look for star-rating Two class within it use dot for space
# print(book_info[0].select('a')[1]['title'])

for i in range(1,51): # there are 50 pages
    url = base_url.format(i)
    result = requests.get(url)
    soup = bs4.BeautifulSoup(result.text, 'lxml')
    book_info = soup.select('.product_pod')
    for book in book_info:
        if len(book.select('.star-rating.Two')) != 0:
            title = book.select('a')[1]['title']
            two_star_titles.append(title)


print(two_star_titles)
import requests
import bs4

base_url = 'https://quotes.toscrape.com/page/{}/'
page_count = 1
authors = set() # toavoid repitition
quotes = []
page_valid = True

# url = base_url.format(page_count)
# result = requests.get(url)
# soup = bs4.BeautifulSoup(result.text, 'lxml')
# quote_block = soup.select('.text')
# quote = quote_block[0].text
# print(quote)

while page_valid:
    url = base_url.format(page_count)
    result = requests.get(url)

    if 'No quotes found!' in result.text:
        break

    soup = bs4.BeautifulSoup(result.text, 'lxml')
    for name in soup.select('.author'):
        authors.add(name.text)
    
    for quote in soup.select('.text'):
        quotes.append(quote.text)

    page_count += 1

print('Authors are : ')
print(authors)
print('Quotes are : ')
print(quotes)
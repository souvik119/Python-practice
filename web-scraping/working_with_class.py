# soup selection 
# soup.select('div') -> all elements with 'div' tag
# soup.select('#some_id') -> elements containing id='some_id'
# soup.select('.some_class') -> elements containing class='some_class'
# soup.select('div span') -> any elements named span within a div element
# soup.select('div>span') -> any element named span directly within a div element nothing in between

#grab all elements of a class (in this case text from table of contents)
import requests
import bs4

result = requests.get('https://en.wikipedia.org/wiki/Real_Madrid_CF')
soup = bs4.BeautifulSoup(result.text, 'lxml')
for item in soup.select('.toctext'): # . for class
    print(item.text)
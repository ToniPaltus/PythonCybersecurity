import requests
from bs4 import BeautifulSoup

# 1 Sample page
'''
url = 'sample_page.html'
with open(url) as file:
    soup = BeautifulSoup(file, 'html.parser')

print(soup.prettify())
print(soup.title, end='\n' + '_'*40 + '\n')
print(soup.title.name, end='\n' + '_'*40 + '\n')
print(soup.title.string, end='\n' + '_'*40 + '\n')
print(soup.title.parent.name, end='\n' + '_'*40 + '\n')
print(soup.p, end='\n' + '_'*40 + '\n')
print(soup.p['class'], end='\n' + '_'*40 + '\n')
print(soup.a, end='\n' + '_'*40 + '\n')
print(soup.find_all('a'), end='\n' + '_'*40 + '\n')
print(soup.find(id='link4'))
'''

# 2 скрапинг https://quotes.toscrape.com/
'''
url = 'https://quotes.toscrape.com/'
#response = requests.get(url).text
#soup = BeautifulSoup(response, 'lxml')

#print(soup, type(soup))# неотформатированный код супом
#print(response, type(response))# отформатированный код строкой
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
#print(soup, type(soup))# слегка отформатированный суп
#print(response, type(response))#<Response [200]> <class 'requests.models.Response'>

quotes = soup.find_all('span', class_='text')
#print(quotes)
for quote in quotes:
    #print(quote.text)
    pass

authors = soup.find_all('small', class_='author')
for i in range(0, len(quotes)):
    #print(quotes[i].text)
    #print('--' + authors[i].text)
    #print()
    pass

tags = soup.find_all('div', class_='tags')
for i in range(len(quotes)):
    print(quotes[i].text)
    print('--' + authors[i].text)
    tags_for_quote = tags[i].find_all('a', class_='tag')
    for tag_for_quote in tags_for_quote:
        print(tag_for_quote.text)
    print()
'''

# 3 парсинг https://scrapingclub.com/exercise/list_basic/?page=1 c учетом пагинации
#url = 'https://scrapingclub.com/exercise/list_basic/?page=1'

#1способ
'''
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
items = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')

for n, i in enumerate(items, start=1):
    itemName = i.find('h4', class_='card-title').text.strip()
    itemPrice = i.find('h5').text
    print(f'{n}: {itemPrice} за {itemName}')

pages = soup.find('ul', class_='pagination')
urls = []
links = pages.find_all('a', class_="page-link")

for link in links:
    pageNum = int(link.text) if link.text.isdigit() else None
    if pageNum != None:
        hrefval = link.get('href')
        urls.append(hrefval)

for slug in urls:
    newUrl = url.replace('?page=1', slug)
    response = requests.get(newUrl)
    soup = BeautifulSoup(response.text, 'lxml')
    items = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')
    for n, i in enumerate(items, start=n):
        itemName = i.find('h4', class_='card-title').text.strip()
        itemPrice = i.find('h5').text
        print(f'{n}: {itemPrice} за {itemName}')
'''

#2 способ
'''
params = {'page': 1}
#задаем число больше номера первой страницы, для старта цикла
pages = 2
n = 1

while params['page'] <= pages:
    response = requests.get(url, params=params)
    soup = BeautifulSoup(response.text, 'lxml')
    items = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')

    for n, i in enumerate(items, start=n):
        itemName = i.find('h4', class_='card-title').text.strip()
        itemPrice = i.find('h5').text
        print(f'{n}: {itemPrice} за {itemName}')
    # [-2] предпоследнее значение, потому что последнее "Next"
    last_page_num = int(soup.find_all('a', class_='page-link')[-2].text)
    pages = last_page_num if pages < last_page_num else pages
    params['page'] += 1
'''

url = 'https://www.rt.com/uk/'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

#parse all - print all
#print(soup.prettify())

#Example 1
'''
#get data by pattern and print it as is
print()
rt_news = soup.find_all('div', class_='card__summary')
print(rt_news)

#print text value
print()
for r in rt_news:
    print(r.text)
'''

#Example 2
'''
#get data by pattern and print only links
print()
for link in soup.find_all('a', class_="link link_hover"):
    print(link.get('href'))
    pass
#print text value
print()
li = soup.find_all('a', class_="link link_hover")
for l in li:
    print(l.text)
'''

#Example 3
'''
#get data by pattern and print it as is
print()
rt_news = soup.find_all('div', class_='card-rows__content')
print(rt_news)
#print text value
print("_+-+-+-+-+-+-++-+-++--+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
for r in rt_news:
    print(r.text)
'''

#Example 4
'''
#print text value
#get data by pattern and print it as is
response1 = requests.get(url)
soup1 = BeautifulSoup(response1.text, 'lxml')
print()
dt = soup1.find_all('span', class_='date')
print(dt)
print()
print(type(dt))
print()
result = []
for data in dt:
    result.append(data.text)
print(result)
'''

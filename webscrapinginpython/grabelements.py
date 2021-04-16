import requests
import bs4

result = requests.get('http://www.example.com')

#print(type(result))

#print(result.text)

soup = bs4.BeautifulSoup(result.text,"lxml")

#print(soup)

#print(soup.select('title'))

#print(soup.select('title')[0].getText())

site_paras = soup.select('p')
print(site_paras)

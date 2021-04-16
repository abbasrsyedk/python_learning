import requests
import bs4

res = requests.get('https://en.wikipedia.org/wiki/Yuvraj_Singh')

soup = bs4.BeautifulSoup(res.text,"lxml")
soup_classtoc = soup.select('.toctext')[0]

print(soup_classtoc)

for item in soup.select('.toctext'):
    print(item.text)
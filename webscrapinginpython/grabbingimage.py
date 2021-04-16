import requests
import bs4

result = requests.get("https://en.wikipedia.org/wiki/Yuvraj_Singh")

soup = bs4.BeautifulSoup(result.text,"lxml")

# src_img = soup.select("img")
# print(src_img)

#grabbing image from a class
# print(soup.select('.infobox-image'))

yuvrajsingh = soup.select('.infobox-image')[0]
print(yuvrajsingh['src'])
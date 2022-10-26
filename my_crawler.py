from bs4 import BeautifulSoup
from matplotlib.pyplot import title
import requests

url = 'https://www.bilibili.com/v/popular/rank/all'

rep= requests.get(url)
###print(rep)
#print(rep.text)
html_text = rep.text
soup = BeautifulSoup(html_text,'html.parser')
items = soup.findAll('li',{'class':'rank-item'})
#items = soup.findAll('li')
#print(soup.title.text)
print(len(items))
for itm in items:
    title = itm.find('a',{'class':'title'}).text
    rank = itm.find('i',{'class':'num'}).text
    visit = itm.find('span',{'class':'data-box'}).text
    #up = itm.find_all('a')[2].text
    #up_id = itm.find_all('a')[2].get('href')[len('//space.bilibili.com/'):]
    url = itm.find('a',{'class':'title'}).get('href')
    #print(f'{rank}.{visit}')
    print(url)

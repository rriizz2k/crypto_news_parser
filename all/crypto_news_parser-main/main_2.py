#Получение ссылок со всеми новостями


import requests
from bs4 import BeautifulSoup




def get_hrefs():
    r = requests.get('https://www.rbc.ru/crypto/')
    soup = BeautifulSoup(r.text, "lxml")
    titles = soup.find_all("div", class_='item js-index-exclude')
    #print(titles)
    res = []
    for title in titles:
        tag_a = title.find('a')
        href = tag_a.get('href')


        res.append(href)
    return res



print(get_hrefs())
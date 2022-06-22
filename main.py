import requests
from bs4 import BeautifulSoup


r = requests.get('https://www.rbc.ru/crypto/')

#---cheack---
#print(r.text)
#print(r.status_code)
#------------

soup = BeautifulSoup(r.text, "lxml")

titles = soup.find_all("span", class_='item__title rm-cm-item-text')
n = 0
for title in titles:
    n +=1
    #print('(',n, ')', title.text.strip())

def get_titles():
    r = requests.get('https://www.rbc.ru/crypto/')
    soup = BeautifulSoup(r.text, "lxml")
    titles = soup.find_all("span", class_='item__title rm-cm-item-text')
    res = []
    for title in titles:
        res.append(title.text.strip())
    return res




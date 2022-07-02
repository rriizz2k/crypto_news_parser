import requests
from bs4 import BeautifulSoup
from keys import keys
from remove_ads import cleaning_ads
import copy
import telegram_send
import yagmail

def send_email(href, title, new, reason):
    f1 = ""
    for i in new:
        f1 += str(i) + ""
    new = f1


    yag = yagmail.SMTP('cryptonewssender', 'xssjltxfjmbusqew')
    contents = [
        new, href
    ]
    yag.send('cryptonewssender@gmail.com', title, contents)

    # Alternatively, with a simple one-liner:
    #yagmail.SMTP('cryptonewssender').send('cryptonewssender@gmail.com', title, contents)








def get_hrefs():
    r = requests.get('https://www.rbc.ru/crypto/')
    soup = BeautifulSoup(r.text, "lxml")
    titles = soup.find_all("div", class_='item item_big js-index-exclude')
    #print(titles)
    res = []
    for title in titles:
        tag_a = title.find('a', class_='item__link')
        #print(tag_a)
        href = tag_a.get('href')
        res.append(href)
    #----second part
    titles1 = soup.find_all("div", class_='item js-index-exclude')

    for title1 in titles1:
        #print('===============', title1)
        tag = title1.find('a', class_='item__link')
        #print('=--=-=-=-=-=-=-=-=-=-=-=-=-=-=0=-=-=-=-=-=-=-=-=-=-=-=',tag)
        #print(tag_a)
        href = tag.get('href')
        res.append(href)

    #----3-rd       part
    titles3 = soup.find_all("a", class_='item__link')
    #print(titles3)
    for title3 in titles3:
        href = title3.get('href')
        res.append(href)



    return res


def get_news():
    hrefs = get_hrefs()
    sended = []
    for href in hrefs:
        fit = False
        print('HREF starterd         --STARTED--')
        #=======================================================
        r = requests.get(href)
        soup = BeautifulSoup(r.text, "lxml")
        print(href)




        title = soup.find('div', class_='article__header__title').text.strip()
        print(title)

        all_text_final = []
        all_txts_p = soup.find_all('p')
        for all_txt in all_txts_p:
            txt = all_txt.text.strip()
            all_text_final.append(txt)
        f1 = ""
        for i in all_text_final:
            f1 += str(i) + " "


        text = copy.copy(f1)

        new = f1.split()
        new = cleaning_ads(new)

        f = ""
        for i in new:
            f += str(i) + " "
        new = f
        print(new)

        if title not in sended:
            for i in keys:
                if i in new:
                    print('из за', i)
                    reason = i
                    f1 = ""
                    for i in new:
                        f1 += str(i) + ""
                    new = f1
                    send_email(href, title, new, reason)
                    sended.append(title)
                    fit = True





        if fit == True:
            print('это новость должна быть отправлена!!!!')
        #=======================================================
        print('HREF closed            --CLOSED--')
        print('---')






print('Our hrefs:', get_hrefs())
print('NEXT FUNCTION:')
print('==============================================================================================================')
get_news()






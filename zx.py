import requests
from bs4 import BeautifulSoup
from time import sleep
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'}

catalog = ['/catalog/78873/', '/catalog/78931/', '/catalog/78936/', '/catalog/78951/', '/catalog/79038/',
          '/catalog/79050/', '/catalog/79246/', '/catalog/79261/', '/catalog/79298/', '/catalog/79326/',
          '/catalog/79340/', '/catalog/79374/', '/catalog/79379/', '/catalog/79379/', '/catalog/79383/',
          '/catalog/79388/', '/catalog/79470/', '/catalog/79525/', '/catalog/79536/', '/catalog/79594/']
category = ['/catalog/78874/', '/catalog/78895/', '/catalog/78896/', '/catalog/78897/', '/catalog/78898/', '/catalog/78899/', '/catalog/78913/', '/catalog/78917/', '/catalog/78927/', '/catalog/78932/', '/catalog/78933/', '/catalog/78934/', '/catalog/78935/', '/catalog/78937/', '/catalog/78938/', '/catalog/78941/', '/catalog/78942/', '/catalog/78943/', '/catalog/78944/', '/catalog/78945/', '/catalog/78946/', '/catalog/78947/', '/catalog/78948/', '/catalog/78949/', '/catalog/78950/', '/catalog/78952/', '/catalog/78953/', '/catalog/78954/', '/catalog/78960/', '/catalog/78961/', '/catalog/78962/', '/catalog/78975/', '/catalog/78976/', '/catalog/78998/', '/catalog/78999/', '/catalog/79010/', '/catalog/79011/', '/catalog/79012/', '/catalog/79678/', '/catalog/79029/', '/catalog/79032/', '/catalog/79039/', '/catalog/79040/', '/catalog/79041/', '/catalog/79042/', '/catalog/79043/', '/catalog/79044/', '/catalog/79045/', '/catalog/79046/', '/catalog/79047/', '/catalog/79048/', '/catalog/79049/', '/catalog/79051/', '/catalog/79060/', '/catalog/79062/', '/catalog/79064/', '/catalog/79073/', '/catalog/79077/', '/catalog/79148/', '/catalog/79164/', '/catalog/79169/', '/catalog/79177/', '/catalog/79184/', '/catalog/79195/', '/catalog/79209/', '/catalog/79247/', '/catalog/79249/', '/catalog/79250/', '/catalog/79251/', '/catalog/79252/', '/catalog/79253/', '/catalog/79254/', '/catalog/79255/', '/catalog/79256/', '/catalog/79257/', '/catalog/79258/', '/catalog/79259/', '/catalog/79260/', '/catalog/79699/', '/catalog/79700/', '/catalog/79262/', '/catalog/79271/', '/catalog/79276/', '/catalog/79287/', '/catalog/79299/', '/catalog/79300/', '/catalog/79305/', '/catalog/79713/', '/catalog/79310/', '/catalog/79323/', '/catalog/79324/', '/catalog/79325/', '/catalog/79327/', '/catalog/79328/', '/catalog/79329/', '/catalog/79330/', '/catalog/79695/', '/catalog/79331/', '/catalog/79332/', '/catalog/79333/', '/catalog/79337/', '/catalog/79338/', '/catalog/79706/', '/catalog/79339/', '/catalog/79341/', '/catalog/79342/', '/catalog/79346/', '/catalog/79353/', '/catalog/79354/', '/catalog/79355/', '/catalog/79360/', '/catalog/79363/', '/catalog/79366/', '/catalog/79367/', '/catalog/79368/', '/catalog/79371/', '/catalog/79372/', '/catalog/79373/', '/catalog/79375/', '/catalog/79376/', '/catalog/79377/', '/catalog/79378/', '/catalog/79380/', '/catalog/79381/', '/catalog/79382/', '/catalog/79712/', '/catalog/79380/', '/catalog/79381/', '/catalog/79382/', '/catalog/79712/', '/catalog/79384/', '/catalog/79385/', '/catalog/79386/', '/catalog/79387/', '/catalog/79389/', '/catalog/79390/', '/catalog/79391/', '/catalog/79404/', '/catalog/79427/', '/catalog/79430/', '/catalog/79431/', '/catalog/79436/', '/catalog/79437/', '/catalog/79438/', '/catalog/79444/', '/catalog/79445/', '/catalog/79449/', '/catalog/79450/', '/catalog/79451/', '/catalog/79460/', '/catalog/79469/', '/catalog/79471/', '/catalog/79477/', '/catalog/79512/', '/catalog/79521/', '/catalog/79526/', '/catalog/79527/', '/catalog/79528/', '/catalog/79529/', '/catalog/79530/', '/catalog/79531/', '/catalog/79532/', '/catalog/79533/', '/catalog/79534/', '/catalog/79535/', '/catalog/79537/', '/catalog/79540/', '/catalog/79542/', '/catalog/79545/', '/catalog/79554/', '/catalog/79560/', '/catalog/79567/', '/catalog/79571/', '/catalog/79572/', '/catalog/79573/', '/catalog/79574/', '/catalog/79575/', '/catalog/79589/', '/catalog/79595/', '/catalog/79598/', '/catalog/79604/', '/catalog/79607/', '/catalog/79617/', '/catalog/79639/', '/catalog/79644/', '/catalog/79649/', '/catalog/79651/', '/catalog/79656/', '/catalog/79674/']
# поиск каталогов
#for c in catalog:
#    url = f'https://stroy-s.org{c}'
#    reaponse = requests.get(url, headers=headers)
#    soup = BeautifulSoup(reaponse.text, 'lxml')
#    map = soup.find_all('a', class_='categories__link')
#    for i in range(len(map)):
#        category.append(map[i].get('href'))

#print(len(category), category)
for t in category:
    url = f'https://stroy-s.org{t}'
    reaponse = requests.get(url, headers=headers)
    soup = BeautifulSoup(reaponse.text, 'lxml')
    title = soup.find('h1', class_='categories__title pagetitle').text.strip()
    pages = soup.find_all('a', class_='category__pagiItem')
    number = pages.find()
    print(title, pages)






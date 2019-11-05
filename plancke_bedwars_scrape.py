from bs4 import BeautifulSoup
import json
import time
import os
import requests

path = os.path.abspath("bedwars.html")

with open(path, 'rb') as bedwars:
    soup = BeautifulSoup(bedwars)

data = []

table = soup.find('table')
table_body = table.find('tbody')
rows = table_body.find_all('tr')

for row in rows:
    cols = row.find_all('td')
    cols2 = []
    for element in cols:
        if element.find('a') != None:
            cols2.append(element.find('a').get('href'))
        cols2.append(element.text.strip())
    data.append([element for element in cols2 if element])

for pt in data[239:240]:
    response = requests.get(pt[1])
    playerdata = response.content
    with open(f'players/player-{pt[0]}.html', 'wb') as p:
        p.write(playerdata)
    time.sleep(1)

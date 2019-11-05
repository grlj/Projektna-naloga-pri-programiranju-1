from bs4 import BeautifulSoup
import json
import time
import os
import requests
import csv

path = os.path.abspath("bedwars_overall.html")

with open(path, 'rb') as bedwars:
    soup = BeautifulSoup(bedwars)

table = soup.find('table')
table_body = table.find('tbody')
rows = table_body.find_all('tr')
data = []

for row in rows:
    cols = row.find_all('td')
    cols = [col.text.strip() for col in cols]
    for i in range(4):
        cols[i+2] = int(str(cols[i+2]).replace(',', ''))
    data.append(cols)

with open('overall.csv', 'w', newline='', encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(data)

# for i in range(1, 1001):
#     with open(f'players/player-{i}.html', 'rb') as pl:
#         soup_pl = BeautifulSoup(pl)


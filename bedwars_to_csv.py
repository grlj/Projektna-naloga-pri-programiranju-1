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
data = [["Id", "[Rank] Name [Guild]", "Wins", "BW Level", "Kills", "Final Kills", "W/L", "K/D", "FK/D"]]

for row in rows:
    cols = row.find_all('td')
    cols = [col.text.strip() for col in cols]
    for i in range(4):
        cols[i+2] = int(str(cols[i+2]).replace(',', ''))
    data.append(cols)

with open('csv/overall.csv', 'w', newline='', encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(data)

collected_general_stats = [["Id", "Coins", "Current Winstreak", "Current Level", "Diamonds Collected", "Emeralds Collected", "Gold Collected", "Iron Collected"]]
collected_solo_stats = [["Id", "K", "D", "K/D", "FK", "FD", "FK/D", "W", "L", "W/L", "Beds Broken"]]
collected_duo_stats = [["Id", "K", "D", "K/D", "FK", "FD", "FK/D", "W", "L", "W/L", "Beds Broken"]]
collected_triple_stats = [["Id", "K", "D", "K/D", "FK", "FD", "FK/D", "W", "L", "W/L", "Beds Broken"]]
collected_quad_stats = [["Id", "K", "D", "K/D", "FK", "FD", "FK/D", "W", "L", "W/L", "Beds Broken"]]
for i in range(1, 1001):
    with open(f'players/player-{i}.html', 'rb') as pl:
        soup_pl = BeautifulSoup(pl)
    
    div_pl = soup_pl.find("div", {"id": "stat_panel_BedWars"}).find('div', {"class" : "panel-body"})

    general_stats = div_pl.find_all('li')
    general_stats.pop(3)
    for j in range(len(general_stats)):
        general_stats[j].b.decompose()
        general_stats[j] = int(str(general_stats[j].text).replace(',', '').replace(' ', ''))
    collected_general_stats.append([i]+general_stats)

    stats_rows = div_pl.find_all('tr')
    for stats, n in [(collected_solo_stats, 2), (collected_duo_stats, 3), (collected_triple_stats, 4), (collected_quad_stats, 5)]:
        drek = stats_rows[n].find_all('td')
        stats.append([i]+[int(str(drek[k].text).replace(',','')) if k in [0,1,3,4,6,7,9] else drek[k].text for k in range(len(drek))])

with open('csv/general.csv', 'w', newline='', encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(collected_general_stats)

with open('csv/solo.csv', 'w', newline='', encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(collected_solo_stats)

with open('csv/duo.csv', 'w', newline='', encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(collected_duo_stats)

with open('csv/triple.csv', 'w', newline='', encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(collected_triple_stats)

with open('csv/quad.csv', 'w', newline='', encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(collected_quad_stats)



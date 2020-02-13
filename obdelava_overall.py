import os
import requests
import csv

path = os.path.abspath("csv/overall.csv")

data = [["Id", "Rank", "Name", "Guild", "Wins", "BW Level", "Kills", "Final Kills", "W/L", "K/D", "FK/D"]]

with open(path, newline='', encoding='utf-8') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        if row == ['Id', ' [Rank] Name [Guild]', ' Wins', ' BW Level', ' Kills', ' Final Kills', ' W/L', ' K/D', ' FK/D']:
            pass
        else: 
            test = []
            for i in range(len(row)):
                if i != 1:
                    test.append(row[i])
                else:
                    x = row[i]
                    x = (x.lstrip(' ')).split(' ')
                    if x[0][0] == '[':
                        test.append(x[0])
                        test.append(x[1])
                        if len(x) == 3:
                            test.append(x[2])
                        else:
                            test.append("None")
                    elif len(x) == 2:
                        test.append("None")
                        test.append(x[0])
                        test.append(x[1])
                    else:
                        test.append("None")
                        test.append(x[0])
                        test.append("None")
            data.append(test)

with open('csv/overallFIXED.csv', 'w', newline='', encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(data)

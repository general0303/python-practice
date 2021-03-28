import urllib.request
import re
import matplotlib.pyplot as plt


url = 'https://raw.githubusercontent.com/Newbilius/Old-Games_DOS_Game_Gauntlet/master/GAMES.csv'
resp = urllib.request.urlopen(url)
respData = resp.read()
str = str(respData.decode())
str1 = re.split(';|\n', str)
dates = str1[3::4]
genres = str1[1::4]
setdates = sorted(set(dates))
setgenres = sorted(set(genres))
dDates = dict.fromkeys(setdates, 0)
dGenres = dict.fromkeys(setgenres, 0)
for i in range(len(dates)):
    dDates[dates[i]] += 1
for i in range(len(genres)):
    dGenres[genres[i]] += 1

fig, axs = plt.subplots(2, figsize=(25, 10))
axs[0].bar(setdates, list(dDates.values()))
axs[1].bar(setgenres, list(dGenres.values()))
plt.show()

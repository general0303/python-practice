import email.utils
import json
import urllib.request
import datetime
import random
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


def generate_groups():
    letter = ['К', 'В', 'М', 'Н']
    maxCount = [25, 13, 2, 10]
    result = []
    for i in range(len(letter)):
        for j in range(maxCount[i]):
            result.append(letter[i] + str(j + 1))
    return result


def generate_tasks():
    letter = 'f'
    maxCount = [4, 3, 2]
    result = []
    for i in range(len(maxCount)):
        for j in range(maxCount[i]):
            result.append(letter + str(i + 1) + str(j + 1))
    return result


def diff(ones, zeros):
    result = []
    for i in range(len(ones)):
        result.append(ones[i]-zeros[i])
    return result

with urllib.request.urlopen('https://raw.githubusercontent.com/true-grue/kispython/main/pract3/table.json') as url:
    table = json.loads(url.read().decode())  # Таблица решений задач
with urllib.request.urlopen('https://raw.githubusercontent.com/true-grue/kispython/main/pract3/failed.json') as url:
    failed = json.loads(url.read().decode())  # Данные по ошибкам
with urllib.request.urlopen('https://raw.githubusercontent.com/true-grue/kispython/main/pract3/messages.json') as url:
    messages = json.loads(url.read().decode())  # Полученные сообщения
messages = [(m['subj'].upper(), email.utils.parsedate(m['date'])) for m in messages]

time = [datetime.datetime(2021, 3, 21, messages[i][1][3], messages[i][1][4], messages[i][1][5]) for i in
        range(len(messages))]
count = list(range(24))
for i in range(len(time)):
    count[time[i].time().hour] += 1

x = [datetime.datetime(2021, 3, 21) + datetime.timedelta(hours=i) for i in range(24)]
y = count

plt.plot(x, y)
plt.gcf().autofmt_xdate()
myFmt = mdates.DateFormatter('%H:%M')
plt.gca().xaxis.set_major_formatter(myFmt)

plt.show()
plt.close()

# messages[var][0].split()[0] - группа
d = dict.fromkeys(generate_groups(), 0)
for i in range(len(messages)):
    key = messages[i][0].split()[0].upper()
    d[key] += 1

x = generate_groups()
y = list(d.values())
plt.subplots(figsize=(20,10))
plt.bar(x, y)
plt.show()


print(table['data'][0][3])
# table['data'][var][0] - группа
# table['data'][var][3] - оценка


d = dict.fromkeys(generate_groups(), 0)
for i in range(len(table['data'])):
    score = table['data'][i][3]
    if score == 1:
        key = table['data'][i][0]
        d[key] += 1
x = generate_groups()
y = list(d.values())
plt.subplots(figsize=(20,10))
plt.bar(x, y)
plt.show()

with urllib.request.urlopen('https://raw.githubusercontent.com/true-grue/kispython/main/pract3/messages.json') as url:
    messages = json.loads(url.read().decode())

count = list(range(7))
for i in range(len(messages)):
    day = messages[i]['date'][:3]
    if day == 'Mon':
        count[0] += 1
    elif day == 'Tue':
        count[1] += 1
    elif day == 'Wed':
        count[2] += 1
    elif day == 'Thu':
        count[3] += 1
    elif day == 'Fri':
        count[4] += 1
    elif day == 'Sat':
        count[5] += 1
    elif day == 'Sun':
        count[6] += 1

days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

x = days
y = count
plt.subplots()
plt.bar(x, y)
plt.show()


# table['data'][var][2] - задание
# table['data'][var][3] - оценка


dZero = dict.fromkeys(generate_tasks(), 0)
dOne = dict.fromkeys(generate_tasks(), 0)
for i in range(len(table['data'])):
    score = table['data'][i][3]
    key = table['data'][i][2]
    if score == 0:
        dZero[key] += 1
    else:
        dOne[key] += 1
x = generate_tasks()
y = diff(list(dOne.values()), list(dZero.values()))
plt.subplots()
plt.title('Разность между кол-вом 1 и 0/Задача')
plt.bar(x, y)
plt.show()

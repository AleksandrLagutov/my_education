import requests
import json
import sys


client_id = '62e6a3e565ee7375b3aa'
client_secret = 'e701271dd5a3409038e4e3fc91c7d246'
token = '4d8b92b34eb68a1b2c0003f4'

# инициируем запрос на получение токена
r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                  data={
                      "client_id": client_id,
                      "client_secret": client_secret
                  })

# разбираем ответ сервера
j = json.loads(r.text)
# достаем токен
# достаем токен
token = j["token"]
# создаем заголовок, содержащий наш токен
headers = {"X-Xapp-Token" : token}
# инициируем запрос с заголовком
dict_of_arts = []
for i in sys.stdin:
    if i == ('\n'):
        break
    url= "https://api.artsy.net/api/artists/{}".format(i.strip())
    r = requests.get(url, headers=headers)

    # разбираем ответ сервера
    j = json.loads(r.text)
    dict_of_arts.append([j['sortable_name'],j['birthday']])
dict_of_arts.sort(key=lambda birt: birt[1])
for i in dict_of_arts:
    print(i[0])
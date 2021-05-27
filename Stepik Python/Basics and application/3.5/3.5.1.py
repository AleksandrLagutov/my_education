import requests
import json
import sys
for i in sys.stdin:
    Num = int(i.strip())
    print(Num)
    api_url = 'http://numbersapi.com/{}/math'.format(Num)

    params = {
        'json': 'true',

    }
    res = requests.get(api_url,params=params)
    print(res.status_code)
    print(res.text)

    data = res.json()
    print(data['found'])
    if data['found']:
        print('Interesting')
    else:
        print('Boring')
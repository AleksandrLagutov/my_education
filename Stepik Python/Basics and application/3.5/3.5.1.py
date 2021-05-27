import requests
import json
import sys
for i in sys.stdin:
    Num = int(i.strip())
    api_url = 'http://numbersapi.com/{}/math'.format(Num)
    params = {
        'json': 'true',
    }
    res = requests.get(api_url,params=params)
    data = res.json()
    if data['found']:
        print('Interesting')
    else:
        print('Boring')
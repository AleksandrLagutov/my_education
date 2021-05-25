import requests
import re
url1 = "https://stepic.org/media/attachments/lesson/24472/sample0.html"
url2 = "https://stepic.org/media/attachments/lesson/24472/sample2.html"
def get_list_url(url):
    res = requests.get(url)
    result = []
    if res.status_code == 200:
        intxt = res.text
        regular = r"https.+\.html"
        next_u = re.findall(regular, intxt)
        for _ in next_u:
            resp = requests.get(_)
            if resp.status_code == 200:
                intxt1 = resp.text
                regular = r"https.+\.html"
                result +=(re.findall(regular, intxt1))

    return result
def resalt(list_url,url2):
    if url2 in list_url:
        print('Yes')
    else:
        print('No')
resalt(get_list_url(url1),url2)
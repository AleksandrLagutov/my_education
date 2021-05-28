import re
import requests
inp_url = input('Input URL\n')
pattern = r"<a.*?href[ ]?=['\"](?:http[s]?://|ftp://|)([^.](?:\w*[-.]+\w+)+)"
res = requests.get(inp_url)

inp_text = res.text
#with open('inf.html', 'r') as inpf:
    #text_html = inpf.read()
url = re.findall(pattern, inp_text)
url = list(set(url))

url.sort()
for i in url:
    print(i)


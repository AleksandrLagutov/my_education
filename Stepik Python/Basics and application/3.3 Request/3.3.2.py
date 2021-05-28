import re
import requests
inp_url = "http://pastebin.com/raw/hfMThaGb"
pattern = r"<a.*?href[ ]?=['\"](?:http[s]?://|ftp://|)([^.](?:\w*[-.]+\w+)+)"
res = requests.get(inp_url)
print(res.status_code)
inp_text = res.text
#with open('inf.html', 'r') as inpf:
    #text_html = inpf.read()
print(inp_text)
url = re.findall(pattern, inp_text)
url = list(set(url))

url.sort()
for i in url:
    print(i)

#Login<a href="http://steeeeeeepic.org/courses">

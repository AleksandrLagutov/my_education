import re
import requests

pattern = r'<a[^>]*?href="(.*?)"[^>]*?>'
list_url = []
with open('inf.html', 'r') as inpf:
    text_html = inpf.read()
    print(text_html)
    url = re.findall(pattern, text_html)
print(url)
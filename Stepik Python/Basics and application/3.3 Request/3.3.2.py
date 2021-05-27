import re
import requests

pattern = r'<a[^>]*?href=[\'"]([\w*?://]*[\w*\-\w*\.*]+)'
list_url = []
with open('inf.html', 'r') as inpf:
    text_html = inpf.read()
    print(text_html)
    url = re.findall(pattern, text_html)
print(url)

#Login<a href="http://steeeeeeepic.org/courses">
https://regex101.com/r/gFBb8y/17
<a.+href=[\"']https://|ftp://|([\w*\.\w*]+)['\"].*>
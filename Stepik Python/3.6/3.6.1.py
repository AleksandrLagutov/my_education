import requests
count_line = 0

input_file = requests.get('https://stepic.org/media/attachments/course67/3.6.3/699991.txt')
list_of_txt = input_file.text
url = list_of_txt.splitlines()[0].strip()
print(url[0])
while url[0] != 'W':
    input_file = requests.get('https://stepic.org/media/attachments/course67/3.6.3/' + url)
    list_of_txt = input_file.text
    url = list_of_txt.splitlines()[0]
    print(url)
print(list_of_txt)

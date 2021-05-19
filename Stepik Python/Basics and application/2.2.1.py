import simplecrypt
inf_list = []
with open('passwords.txt') as inf:
    for line in inf:
        inf_list.append(line.strip())
print(inf_list)
with open('encrypted.bin', 'rb') as inp:
    encrypted = inp.read()
password = []
for pas in inf_list:
    try:
        txt = simplecrypt.decrypt(pas, encrypted)
        print(txt)
    except simplecrypt.DecryptionException:
        pass

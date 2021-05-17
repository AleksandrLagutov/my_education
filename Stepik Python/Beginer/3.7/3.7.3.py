d = int(input())
known_words = set(input().lower() for i in range(d))
unknown_words = set()
l = int(input())
for _ in range(l):
    tmp_str = input().split()
    for i in tmp_str:
        if i.lower() not in known_words:
            unknown_words.add(i.lower())
print(unknown_words)


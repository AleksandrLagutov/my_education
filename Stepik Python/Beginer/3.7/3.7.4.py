steps = int(input())
d = {'север': 0, 'запад': 0, 'юг': 0, 'восток': 0}
point = [0, 0]
for _ in range(steps):
    tmp_input = list(i for i in input().split())
    d[tmp_input[0]] += int(tmp_input[1])
print(d['восток']-d['запад'], d['север']-d['юг'])
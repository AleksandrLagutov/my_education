def mark_attack(x, y, c):
    if not (0 < x < 9 and 0 < y < 9):
        return
    c[x][y] = -1

dict = {"a" : 1, "b" : 2, "c" : 3,  "d" : 4,
        "e" : 5, "f" : 6, "g" : 7,  "h" : 8
        }

redict = [0, "a", "b", "c", "d", "e", "f", "g", "h"]
c = [[0]*9 for i in range(0, 9)]
s = input()
knight = (dict[s[0]], int(s[1]))

mark_attack(knight[0],knight[1], c)
mark_attack(knight[0] - 2,knight[1] - 1, c)
mark_attack(knight[0] - 2,knight[1] + 1, c)
mark_attack(knight[0] - 1,knight[1] + 2, c)
mark_attack(knight[0] + 1,knight[1] + 2, c)
mark_attack(knight[0] + 2,knight[1] + 1, c)
mark_attack(knight[0] + 2,knight[1] - 1, c)
mark_attack(knight[0] + 1,knight[1] - 2, c)
mark_attack(knight[0] - 1,knight[1] - 2, c)

c[0][0] = 1

for i in range(1,9):
    for j in range(1,9):
        if c[i][j] == -1:
            continue
        c[i][j] = ((c[i - 1][j] if c[i - 1][j] != -1 else 0)
                    + (c[i][j - 1] if c[i][j - 1] != -1 else 0)
                    + (c[i - 1][j - 1] if c[i - 1][j - 1] != -1 else 0) )


print(c[8][8] if c[8][8] != -1 else 0)

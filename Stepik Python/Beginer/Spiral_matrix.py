"""
data_input = int(input())
data = [[None for i in range(data_input)] for j in range(data_input)]
n = data_input
dx, dy = 1, 0
x, y = 0, 0
for i in range(1,n**2+1):
    data[y][x] = i
    nx, ny = x + dx, y + dy
    if 0 <= nx < n and 0 <= ny < n and data[ny][nx] == None:
        x, y = nx, ny
    else:
        dx, dy = -dy, dx
        x, y = x+dx, y+dy

for _ in range(data_input):
    print(*data[_])
"""
n = int(input())
x,y,dx,dy, m = 0,0,0,1, [[0]*n for i in range(n)]
for i in range(n*n):
  m[x][y]=str(i+1)
  if x+dx>=n or x+dx<0 or y+dy>=n or y+dy<0 or m[x+dx][y+dy]:
      dx,dy = dy,-dx
  x,y = x+dx, y+dy
print("\n".join([" ".join(i) for i in m]))
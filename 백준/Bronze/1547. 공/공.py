m = int(input())
pos = 1 

for _ in range(m):
    x, y = map(int, input().split())
    if pos == x:
        pos = y
    elif pos == y:
        pos = x

print(pos)
import sys

n, m = map(int, sys.stdin.readline().split())

grid = [[0] * 101 for _ in range(101)]

for _ in range(n):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            grid[x][y] += 1

count = sum(1 for x in range(1, 101) for y in range(1, 101) if grid[x][y] > m)
print(count)

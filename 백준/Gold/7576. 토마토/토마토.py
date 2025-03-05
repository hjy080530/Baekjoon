import sys
from collections import deque

M, N = map(int, sys.stdin.readline().split())  
box = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue = deque()

for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            queue.append((i, j))

while queue:
    x, y = queue.popleft()
    
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < N and 0 <= ny < M and box[nx][ny] == 0:
            box[nx][ny] = box[x][y] + 1
            queue.append((nx, ny))

max_days = 0
for row in box:
    if 0 in row:
        print(-1)
        exit()
    max_days = max(max_days, max(row))

print(max_days - 1 if max_days > 1 else 0)
import sys
sys.setrecursionlimit(10000)

n = int(input())
grid = [list(input().strip()) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, color, visited, board):
    visited[x][y] = True
    for d in range(4):
        nx, ny = x + dx[d], y + dy[d]
        if 0 <= nx < n and 0 <= ny < n:
            if not visited[nx][ny] and board[nx][ny] == color:
                dfs(nx, ny, color, visited, board)
visited_normal = [[False]*n for _ in range(n)]
count_normal = 0

for i in range(n):
    for j in range(n):
        if not visited_normal[i][j]:
            dfs(i, j, grid[i][j], visited_normal, grid)
            count_normal += 1

color_blind_grid = [row[:] for row in grid]  # 복사
for i in range(n):
    for j in range(n):
        if color_blind_grid[i][j] == 'G':
            color_blind_grid[i][j] = 'R'

visited_cb = [[False]*n for _ in range(n)]
count_cb = 0

for i in range(n):
    for j in range(n):
        if not visited_cb[i][j]:
            dfs(i, j, color_blind_grid[i][j], visited_cb, color_blind_grid)
            count_cb += 1

print(count_normal, count_cb)
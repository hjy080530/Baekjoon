N, E, W, S, N_ = map(int, input().split())
prob = [E, W, S, N_]

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

visited = [[False]*30 for _ in range(30)]

answer = 0.0

def dfs(x, y, depth, p):
    global answer
    if depth == N:
        answer += p
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if not visited[nx][ny] and prob[i] > 0:
            visited[nx][ny] = True
            dfs(nx, ny, depth+1, p * (prob[i] / 100))
            visited[nx][ny] = False

visited[15][15] = True
dfs(15, 15, 0, 1.0)

print(answer)
n, m = map(int, input().split())
board = [input().strip() for _ in range(n)]

max_size = 1

for i in range(n):
    for j in range(m):
        for l in range(1, min(n - i, m - j)):
            if board[i][j] == board[i][j + l] == board[i + l][j] == board[i + l][j + l]:
                max_size = max(max_size, (l + 1) ** 2)

print(max_size)
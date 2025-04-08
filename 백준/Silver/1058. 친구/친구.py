n = int(input())
g = [list(input()) for _ in range(n)]

def f(i):
    s = set()
    for j in range(n):
        if g[i][j] == 'Y':
            s.add(j)
            for k in range(n):
                if g[j][k] == 'Y' and k != i:
                    s.add(k)
    return len(s)

print(max(f(i) for i in range(n)))
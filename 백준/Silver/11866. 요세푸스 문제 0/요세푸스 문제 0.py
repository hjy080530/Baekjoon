from collections import deque

n, k = map(int, input().split())
q = deque(range(1, n + 1)) 
res = []

while q:
    q.rotate(-(k-1))
    res.append(q.popleft())

print("<" + ", ".join(map(str, res)) + ">")
from collections import deque

def y(n, k):
    q = deque(range(1, n+1))
    r = []
    
    while q:
        q.rotate(-(k-1))  
        r.append(q.popleft())

    print("<" + ", ".join(map(str, r)) + ">")

n, k = map(int, input().split())
y(n, k)
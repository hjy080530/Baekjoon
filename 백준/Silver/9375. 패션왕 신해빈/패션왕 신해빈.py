import sys
from collections import defaultdict

t = int(sys.stdin.readline().strip())

for _ in range(t):
    n = int(sys.stdin.readline().strip())
    d = defaultdict(int)

    for _ in range(n):
        _, c = sys.stdin.readline().strip().split()
        d[c] += 1

    r = 1
    for v in d.values():
        r *= (v + 1)

    print(r - 1)
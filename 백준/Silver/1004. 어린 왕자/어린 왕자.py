import sys
from io import StringIO

def c(px, py, cx, cy, r):
    return (px - cx) ** 2 + (py - cy) ** 2 < r ** 2

def s():
    t = int(sys.stdin.readline().strip())
    r = []
    
    for _ in range(t):
        x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
        n = int(sys.stdin.readline().strip())
        c_ = 0

        for _ in range(n):
            cx, cy, r_ = map(int, sys.stdin.readline().split())
            i1 = c(x1, y1, cx, cy, r_)
            i2 = c(x2, y2, cx, cy, r_)

            if i1 != i2:
                c_ += 1

        r.append(str(c_))
    
    sys.stdout.write("\n".join(r) + "\n")

s()
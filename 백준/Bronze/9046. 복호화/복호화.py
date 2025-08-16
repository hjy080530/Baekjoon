import sys
it = iter(sys.stdin.read().splitlines())
t = int(next(it))
for _ in range(t):
    s = next(it)
    a = [0]*26
    for ch in s.lower():
        if 'a' <= ch <= 'z':
            a[ord(ch)-97] += 1
    m = max(a)
    print(chr(a.index(m)+97) if a.count(m) == 1 else '?')
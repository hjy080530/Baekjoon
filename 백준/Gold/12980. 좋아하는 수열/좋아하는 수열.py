from itertools import permutations

def sc(a): 
    t = 0
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            if a[i] < a[j]:
                t += 1
    return t

n, s = map(int, input().split())
a = list(map(int, input().split()))
used = set(a) - {0}
left = [x for x in range(1, n+1) if x not in used]

z = [i for i, v in enumerate(a) if v == 0]

ans = 0
for p in permutations(left):
    tmp = a[:]
    for i in range(len(z)):
        tmp[z[i]] = p[i]
    if sc(tmp) == s:
        ans += 1

print(ans)
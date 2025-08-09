n = int(input().strip())
p = list(map(int, input().split()))
r = int(input().strip())

children = [[] for _ in range(n)]
root = -1
for i in range(n):
    if p[i] == -1:
        root = i
    else:
        children[p[i]].append(i)

if r == root:
    print(0)
    exit()

ans = 0
stk = [root]
while stk:
    u = stk.pop()
    if u == r:
        continue
    cnt = 0
    for v in children[u]:
        if v == r:
            continue
        cnt += 1
        stk.append(v)
    if cnt == 0:
        ans += 1

print(ans)
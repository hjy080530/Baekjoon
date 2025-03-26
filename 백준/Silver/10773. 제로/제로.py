k = int(input())
s = []

for _ in range(k):
    n = int(input())
    if n == 0:
        s.pop()
    else:
        s.append(n)

print(sum(s))
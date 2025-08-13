def is_han(x):
    if x < 100:
        return True
    if x == 1000:
        return False
    a = x // 100
    b = (x // 10) % 10
    c = x % 10
    return (a - b) == (b - c)

n = int(input())
cnt = 0
for i in range(1, n + 1):
    if is_han(i):
        cnt += 1
print(cnt)
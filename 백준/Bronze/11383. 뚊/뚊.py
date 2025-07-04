n, m = map(int, input().split())

original = [input() for _ in range(n)]
expanded = [input() for _ in range(n)]

is_same = True

for i in range(n):
    doubled = ''.join([ch * 2 for ch in original[i]])
    if doubled != expanded[i]:
        is_same = False
        break

print("Eyfa" if is_same else "Not Eyfa")
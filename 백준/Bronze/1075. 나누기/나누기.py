N = int(input())
F = int(input())

N -= N % 100
while N % F != 0:
    N += 1

print(f"{N % 100:02d}")
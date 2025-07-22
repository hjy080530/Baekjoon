T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    n = A // B
    print(n * n)
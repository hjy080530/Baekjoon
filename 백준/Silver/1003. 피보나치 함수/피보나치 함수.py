def solve():
    t = int(input())
    dp_0 = [0] * 41
    dp_1 = [0] * 41
    
    dp_0[0], dp_1[0] = 1, 0
    dp_0[1], dp_1[1] = 0, 1
    
    for i in range(2, 41):
        dp_0[i] = dp_0[i-1] + dp_0[i-2]
        dp_1[i] = dp_1[i-1] + dp_1[i-2]
    
    for _ in range(t):
        n = int(input())
        print(dp_0[n], dp_1[n])

if __name__ == "__main__":
    solve()
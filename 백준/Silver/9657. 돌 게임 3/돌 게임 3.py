n = int(input())
dp = [False] * (n + 5)

dp[1] = True
dp[2] = False
dp[3] = True
dp[4] = True
dp[5] = True

for i in range(5, n + 1):
    if not (dp[i-1] and dp[i-3] and dp[i-4]):
        dp[i] = True

print("SK" if dp[n] else "CY")
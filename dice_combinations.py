MOD = 10**9 + 7
n = int(input())

dp = [0] * (n+1)
dp[0] = 1
dp[1] = 1
# dp[2] = 2

for i in range(1, n + 1):
    # s = dp[i-1]
    s = 0
    
    for j in range(1, 7):
        if i >= j:
            s += dp[i - j] % MOD
        dp[i] = s % MOD

    # if i <= 6:
        # dp[i] += 1

# print(dp)
print(dp[n])
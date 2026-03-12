MOD = 1_000_000_000


# main
n, k = map(int, input().split())

answer = 0

dp = [[0 for _ in range(n + 1)] for _ in range(k + 1)]

# 숫자 1 ~ k개로 0을 만드는 방법
for i in range(1, k + 1):
    dp[i][0] = 1

# 숫자 1개로 1 ~ n 까지의 합을 만드는 방법
for j in range(1, n + 1):
    dp[1][j] = 1

for i in range(1, k + 1):
    for j in range(1, n + 1):
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

answer = dp[k][n] % MOD

print(answer)

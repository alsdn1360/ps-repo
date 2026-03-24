import sys

sys.setrecursionlimit(10**9)

MOVES = [(-1, 0), (1, 0), (0, 1), (0, -1)]


def in_bound(nx, ny):
    return 0 <= nx < n and 0 <= ny < n


def is_continue(x, y):
    for dx, dy in MOVES:
        nx, ny = x + dx, y + dy

        if in_bound(nx, ny) and bamboo[x][y] < bamboo[nx][ny]:
            return True

    return False


def dfs(x, y):
    if not is_continue(x, y):
        return 1

    if dp[x][y] > 1:
        return dp[x][y]

    for dx, dy in MOVES:
        nx, ny = x + dx, y + dy

        if in_bound(nx, ny) and bamboo[x][y] < bamboo[nx][ny]:
            dp[x][y] = max(dp[x][y], dfs(nx, ny) + 1)

    return dp[x][y]


# main
answer = 0

n = int(input())
bamboo = [list(map(int, input().split())) for _ in range(n)]

dp = [[1 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        answer = max(answer, dfs(i, j))

print(answer)

import sys

input = sys.stdin.readline


MOVES = [(-1, 0), (1, 0), (0, 1), (0, -1)]


def in_bound(nx, ny):
    return 0 <= nx < n and 0 <= ny < m


def dfs(x, y, idx):
    if idx == len(target):
        return 1

    if dp[x][y][idx] != -1:
        return dp[x][y][idx]

    dp[x][y][idx] = 0

    for dx, dy in MOVES:
        for movable in range(1, k + 1):
            nx, ny = x + (dx * movable), y + (dy * movable)

            if in_bound(nx, ny) and board[nx][ny] == target[idx]:
                dp[x][y][idx] += dfs(nx, ny, idx + 1)

    return dp[x][y][idx]


# main
answer = 0

n, m, k = map(int, input().split())
board = [list(input().rstrip()) for _ in range(n)]
target = input().rstrip()

dp = [[[-1 for _ in range(len(target))] for _ in range(m)] for _ in range(n)]

for i in range(n):
    for j in range(m):
        if board[i][j] == target[0]:
            answer += dfs(i, j, 1)

print(answer)

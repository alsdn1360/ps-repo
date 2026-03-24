import sys

sys.setrecursionlimit(10**9)

MOVES = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def in_bound(nx, ny):
    return 0 <= nx < M and 0 <= ny < N


def dfs(x, y):
    if (x, y) == (M - 1, N - 1):
        return 1  # 끝까지 왔으면 경로의 수 한 개 추가

    if dp[x][y] != -1:
        return dp[x][y]  # 이미 방문한 적이 있으면 이전까지의 경로의 수 반환

    dp[x][y] = 0  # 방문 처리

    for dx, dy in MOVES:
        nx, ny = x + dx, y + dy

        if in_bound(nx, ny):
            if grid[x][y] > grid[nx][ny]:
                dp[x][y] += dfs(nx, ny)

    return dp[x][y]


# main
M, N = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(M)]

dp = [[-1 for _ in range(N)] for _ in range(M)]

print(dfs(0, 0))

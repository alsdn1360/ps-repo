MAX_N = 30


def solve(w, h):
    if w == 0:
        return 1

    if drugs[w][h] != 0:
        return drugs[w][h]

    cnt = 0

    cnt += solve(w - 1, h + 1)

    if h > 0:
        cnt += solve(w, h - 1)

    drugs[w][h] = cnt

    return cnt


# main
drugs = [[0 for _ in range(MAX_N + 1)] for _ in range(MAX_N + 1)]

while True:
    n = int(input())

    if n == 0:
        break

    answer = solve(n, 0)

    print(answer)

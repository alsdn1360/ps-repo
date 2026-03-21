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
while True:
    n = int(input())

    if n == 0:
        break

    drugs = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

    answer = solve(n, 0)

    print(answer)

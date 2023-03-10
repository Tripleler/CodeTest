# https://www.acmicpc.net/problem/15650

# from itertools import combinations
#
# n, m = map(int, input().split())
# for x in combinations(range(1, n + 1), m):
#     print(*x)

n, m = map(int, input().split())
arr = []
visit = [False] * n


def back(k, n, m):
    if k == m:
        print(' '.join(map(str, arr)))
        return
    for i in range(arr[-1] if arr else 0, n):
        if not visit[i]:
            visit[i] = True
            arr.append(i + 1)
            back(k + 1, n, m)
            visit[i] = False
            arr.pop()


back(0, n, m)

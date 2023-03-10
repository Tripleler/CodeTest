# https://www.acmicpc.net/problem/15649

# from itertools import permutations
#
# n, m = map(int, input().split())
# for x in permutations(range(1, n + 1), m):
#     print(*x)

n, m = map(int, input().split())
visit = [False] * n
arr = []


def back(k, n, m):
    if k == m:
        print(' '.join(map(str, arr)))
        return
    for i in range(n):
        if not visit[i]:
            visit[i] = True
            arr.append(i + 1)
            back(k + 1, n, m)
            visit[i] = False
            arr.pop()


back(0, n, m)

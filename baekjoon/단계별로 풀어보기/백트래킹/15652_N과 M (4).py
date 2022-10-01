# https://www.acmicpc.net/problem/15652

# from itertools import combinations_with_replacement
#
# n, m = map(int, input().split())
# for x in combinations_with_replacement(range(1, n + 1), m):
#     print(*x)

n, m = map(int, input().split())
arr = []


def back(k, n, m):
    if k == m:
        print(' '.join(map(str, arr)))
        return
    for i in range(arr[-1] if arr else 1, n + 1):
        arr.append(i)
        back(k + 1, n, m)
        arr.pop()


back(0, n, m)

# https://www.acmicpc.net/problem/15651

# from itertools import product
#
# n, m = map(int, input().split())
# for x in product(range(1, n + 1), repeat=m):
#     print(*x)

n, m = map(int, input().split())
arr = []


def back(k, n, m):
    if k == m:
        print(' '.join(map(str, arr)))
        return
    for i in range(n):
        arr.append(i + 1)
        back(k + 1, n, m)
        arr.pop()


back(0, n, m)

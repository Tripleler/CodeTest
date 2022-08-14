# https://www.acmicpc.net/problem/11659

# from sys import stdin
#
# input = stdin.readline
# n, m = map(int, input().split())
# l = list(map(int, input().split()))
# for x in range(1, n):
#     l[x] = l[x] + l[x - 1]
# for _ in range(m):
#     i, j = map(int, input().split())
#     print(l[j - 1] - (l[i - 2] if i != 1 else 0))

from itertools import accumulate
from sys import stdin

input = stdin.readline
n, m = map(int, input().split())
l = list(accumulate(map(int, input().split())))
for _ in range(m):
    i, j = map(int, input().split())
    print(l[j - 1] - (l[i - 2] if i != 1 else 0))

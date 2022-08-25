# https://www.acmicpc.net/problem/1149

from sys import stdin

input = stdin.readline
l = [[0, 0, 0]]
for i in range(1, int(input()) + 1):
    r, g, b = map(int, input().split())
    r = min(l[i - 1][1], l[i - 1][2]) + r
    g = min(l[i - 1][0], l[i - 1][2]) + g
    b = min(l[i - 1][0], l[i - 1][1]) + b
    l.append([r, g, b])
print(min(l[-1]))

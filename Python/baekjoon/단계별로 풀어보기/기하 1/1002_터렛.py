# https://www.acmicpc.net/problem/1002

from sys import stdin

input = stdin.readline
for _ in range(int(input())):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    d = (x2 - x1) ** 2 + (y2 - y1) ** 2
    if d == 0:
        print(-1 if r1 == r2 else 0)
    elif ((r1 + r2) ** 2 == d) or (abs(r1 - r2) ** 2 == d):
        print(1)
    elif ((r1 + r2) ** 2 < d) or (abs(r1 - r2) ** 2 > d):
        print(0)
    else:
        print(2)

# https://www.acmicpc.net/problem/1004

from sys import stdin

input = stdin.readline
for _ in range(int(input())):
    cnt = 0
    x1, y1, x2, y2 = map(int, input().split())
    for _ in range(int(input())):
        cx, cy, r = map(int, input().split())
        if ((cx - x1) ** 2 + (cy - y1) ** 2 < r ** 2) + ((cx - x2) ** 2 + (cy - y2) ** 2 < r ** 2) == 1:
            cnt += 1
    print(cnt)

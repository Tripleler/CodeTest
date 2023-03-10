# https://www.acmicpc.net/problem/11650

from sys import stdin

input = stdin.readline
li = []
for _ in range(int(input())):
    li.append(tuple(map(int, input().split())))
li = sorted(li, key=lambda x: (x[0], x[1]))
for i, j in li:
    print(i, j)

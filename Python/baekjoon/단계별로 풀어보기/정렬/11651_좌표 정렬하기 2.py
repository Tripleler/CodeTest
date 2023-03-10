# https://www.acmicpc.net/problem/11651

from sys import stdin

input = stdin.readline
li = []
for _ in range(int(input())):
    li.append(tuple(map(int, input().split())))
li = sorted(li, key=lambda x: (x[1], x[0]))
for i, j in li:
    print(i, j)

# https://www.acmicpc.net/problem/2751

from sys import stdin

input = stdin.readline
li = []
for _ in range(int(input())):
    li.append(int(input()))
for x in sorted(li):
    print(x)

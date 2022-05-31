# https://www.acmicpc.net/problem/2562

from sys import stdin

input = stdin.readline
li = []
for _ in range(9):
    li.append(int(input()))
print(max(li))
print(li.index(max(li)) + 1)

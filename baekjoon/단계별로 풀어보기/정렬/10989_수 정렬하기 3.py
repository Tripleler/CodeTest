# https://www.acmicpc.net/problem/10989

from sys import stdin

input = stdin.readline
li = [0] * 10000
for _ in range(int(input())):
    li[int(input()) - 1] += 1
for i in range(10000):
    if li[i]:
        for _ in range(li[i]):
            print(i + 1)

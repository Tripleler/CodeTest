# https://www.acmicpc.net/problem/1181

from sys import stdin

input = stdin.readline
li = []
for _ in range(int(input())):
    li.append(input().rstrip())
li = sorted(list(set(li)), key=lambda x: (len(x), x))
for i in li:
    print(i)

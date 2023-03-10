# https://www.acmicpc.net/problem/1620

from sys import stdin

input = stdin.readline
a, b = map(int, input().split())
l = []
dic = {}
for i in range(1, a + 1):
    x = input().rstrip()
    l.append(x)
    dic[x] = i
for _ in range(b):
    x = input().rstrip()
    if x.isdigit():
        print(l[int(x) - 1])
    else:
        print(dic[x])

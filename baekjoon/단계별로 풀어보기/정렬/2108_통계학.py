# https://www.acmicpc.net/problem/2108

from sys import stdin
from collections import Counter

input = stdin.readline
li = []
n = int(input())
for _ in range(n):
    li.append(int(input()))
li.sort()
print(round(sum(li) / n))
print(li[(n - 1) // 2])
li2 = sorted(Counter(li).items(), key=lambda x: (-x[1], x[0]))
print(li[0] if n == 1 else li2[0][0] if li2[0][1] != li2[1][1] else li2[1][0])
print(max(li) - min(li))

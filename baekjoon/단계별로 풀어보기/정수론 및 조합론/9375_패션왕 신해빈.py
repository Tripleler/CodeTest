# https://www.acmicpc.net/problem/9375

from sys import stdin
from collections import Counter

input = stdin.readline
for _ in range(int(input())):
    clothes = []
    for _ in range(int(input())):
        _, a = input().split()
        clothes.append(a)
    clothes = Counter(clothes)
    cnt = 1
    for x in clothes.values():
        cnt *= (x + 1)
    print(cnt - 1)

# https://www.acmicpc.net/problem/1764

from sys import stdin

input = stdin.readline
a, b = map(int, input().split())
A = set()
B = set()
for _ in range(a):
    A.add(input().rstrip())
for _ in range(b):
    B.add(input().rstrip())
u = sorted(list(A.intersection(B)))
print(len(u))
for x in u:
    print(x)

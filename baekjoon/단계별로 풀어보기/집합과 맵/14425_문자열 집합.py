# https://www.acmicpc.net/problem/14425

from sys import stdin

input = stdin.readline
a, b = map(int, input().split())
s = set()
for _ in range(a):
    s.add(input())
cnt = 0
for _ in range(b):
    if input() in s:
        cnt += 1
print(cnt)

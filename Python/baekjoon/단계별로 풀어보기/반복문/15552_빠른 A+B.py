# https://www.acmicpc.net/problem/15552

from sys import stdin

input = stdin.readline
n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    print(a + b)

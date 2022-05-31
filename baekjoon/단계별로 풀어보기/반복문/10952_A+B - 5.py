# https://www.acmicpc.net/problem/10952

from sys import stdin

input = stdin.readline
while True:
    a, b = map(int, input().split())
    if not a:
        break
    print(a + b)

# https://www.acmicpc.net/problem/10951

from sys import stdin

input = stdin.readline
while True:
    try:
        a, b = map(int, input().split())
        print(a + b)
    except ValueError:
        break

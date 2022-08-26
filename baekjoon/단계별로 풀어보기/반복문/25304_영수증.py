# https://www.acmicpc.net/problem/25304

from sys import stdin

input = stdin.readline
X = int(input())
for _ in range(int(input())):
    a, b = map(int, input().split())
    X -= a * b
print('No' if X else 'Yes')

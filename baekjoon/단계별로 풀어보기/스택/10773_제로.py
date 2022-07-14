# https://www.acmicpc.net/problem/10773

from sys import stdin

input = stdin.readline
stack = []
for _ in range(int(input())):
    n = int(input())
    stack.append(n) if n else stack.pop(-1)
print(sum(stack))

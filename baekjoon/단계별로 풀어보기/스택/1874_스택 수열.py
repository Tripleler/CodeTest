# https://www.acmicpc.net/problem/1874

from sys import stdin

input = stdin.readline
stack = []
label = []
answer = []
n = int(input())
for _ in range(n):
    label.append(int(input()))
k = label.pop(0)
for i in range(1, n + 1):
    stack.append(i)
    answer.append('+')
    while stack and stack[-1] == k:
        stack.pop(-1)
        answer.append('-')
        if label:
            k = label.pop(0)
if stack:
    print('NO')
else:
    print('\n'.join(answer))

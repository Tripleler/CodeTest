# https://www.acmicpc.net/problem/10866

from collections import deque
from sys import stdin

input = stdin.readline
q = deque()
for _ in range(int(input())):
    s = input().split()
    if len(s) == 2:
        if s[0] == 'push_front':
            q.appendleft(s[1])
        elif s[0] == 'push_back':
            q.append(s[1])
    else:
        if s[0] == 'pop_front':
            print(q.popleft() if q else -1)
        elif s[0] == 'pop_back':
            print(q.pop() if q else -1)
        elif s[0] == 'size':
            print(len(q))
        elif s[0] == 'empty':
            print(0 if q else 1)
        elif s[0] == 'front':
            print(q[0] if q else -1)
        elif s[0] == 'back':
            print(q[-1] if q else -1)

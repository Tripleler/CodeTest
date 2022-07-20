# https://www.acmicpc.net/problem/18258

from collections import deque
from sys import stdin

input = stdin.readline
q = deque()
for _ in range(int(input())):
    s = input().rstrip()
    if s == 'pop':
        print(q.popleft() if q else -1)
    elif s == 'size':
        print(len(q))
    elif s == 'empty':
        print(0 if q else 1)
    elif s == 'front':
        print(q[0] if q else -1)
    elif s == 'back':
        print(q[-1] if q else -1)
    else:
        q.append(s.split()[-1])

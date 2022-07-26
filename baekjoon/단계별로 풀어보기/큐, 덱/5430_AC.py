# https://www.acmicpc.net/problem/5430

from collections import deque
from sys import stdin

input = stdin.readline
for _ in range(int(input())):
    D = input().rstrip().replace('RR', '')
    _ = input()
    q = input()[1:-2]
    q = deque(q.split(',')) if q else deque()
    R = False
    try:
        for d in D:
            if d == 'R':
                R = False if R else True
            elif d == 'D':
                q.pop() if R else q.popleft()
    except IndexError:
        print('error')
    else:
        ans = list(reversed(q)) if R else list(q)
        print('[' + ','.join(map(str, ans)) + ']')

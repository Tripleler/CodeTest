# https://www.acmicpc.net/problem/1966

from collections import deque
from sys import stdin

input = stdin.readline
for _ in range(int(input())):
    N, M = map(int, input().split())
    Q = deque(list(map(int, input().split())))
    R = deque([x for x in range(N)])
    m = max(Q)
    cnt = 1
    while True:
        n = Q.popleft()
        r = R.popleft()
        if n == m:
            if M == r:
                break
            else:
                m = max(Q)
                cnt += 1
        else:
            Q.append(n)
            R.append(r)
    print(cnt)

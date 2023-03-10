# https://www.acmicpc.net/problem/1021

from collections import deque
from sys import stdin

input = stdin.readline
m, _ = map(int, input().split())
q = deque([x + 1 for x in range(m)])
l = list(map(int, input().split()))
cnt = 0
for i in l:
    n = q.index(i)
    if n <= len(q) // 2:
        q.rotate(-n)
        cnt += n
    else:
        q.rotate(len(q) - n)
        cnt += len(q) - n
    q.popleft()
print(cnt)

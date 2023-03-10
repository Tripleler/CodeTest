# https://www.acmicpc.net/problem/11866

from collections import deque

n, k = map(int, input().split())
q = deque([x + 1 for x in range(n)])
p = []
while q:
    q.rotate(1 - k)
    p.append(str(q.popleft()))
print('<' + ', '.join(p) + '>')

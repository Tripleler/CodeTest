# https://www.acmicpc.net/problem/2164

from collections import deque
q = deque([x + 1 for x in range(int(input()))])
while len(q) != 1:
    q.popleft()
    q.append(q.popleft())
print(q[0])

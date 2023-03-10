# https://www.acmicpc.net/problem/2477

from collections import deque

n = int(input())
q = deque()
for _ in range(6):
    q.append(tuple(map(int, input().split())))
while (q[2][0] != q[4][0]) or (q[3][0] != q[5][0]):
    q.rotate()
print((q[0][1] * q[1][1] - q[3][1] * q[4][1]) * n)

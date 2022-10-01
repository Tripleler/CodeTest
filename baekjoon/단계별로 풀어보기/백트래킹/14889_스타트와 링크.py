# https://www.acmicpc.net/problem/14889

from itertools import combinations
from collections import deque
from sys import stdin

input = stdin.readline
n = int(input())
sq = [list(map(int, input().split())) for _ in range(n)]
q = deque(combinations(range(n), n // 2))
nums = []
while q:
    cnt = 0
    a = q.popleft()
    b = q.pop()
    for x, y in combinations(a, 2):
        cnt += sq[x][y] + sq[y][x]
    for x, y in combinations(b, 2):
        cnt -= sq[x][y] + sq[y][x]
    nums.append(abs(cnt))
print(min(nums))

# https://www.acmicpc.net/problem/24480

import sys
from sys import stdin


def dfs(i):
    global n, graph, visit, cnt
    visit[i] = cnt
    for j in graph[i]:
        if not visit[j]:
            cnt += 1
            dfs(j)


sys.setrecursionlimit(10 ** 9)
input = stdin.readline
n, m, r = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visit = [0] * (n + 1)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(1, n + 1):
    graph[i].sort(reverse=True)
cnt = 1
dfs(r)
print(*visit[1:], sep='\n')

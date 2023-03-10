# https://www.acmicpc.net/problem/1260

from sys import stdin


def dfs(i):
    visit1[i] = True
    print(i, end=' ')
    for j in graph[i]:
        if not visit1[j]:
            dfs(j)


def bfs(i):
    visit2[i] = True
    q = [i]
    print(i, end=' ')
    while q:
        temp = list()
        for j in q:
            for k in graph[j]:
                if not visit2[k]:
                    visit2[k] = True
                    temp.append(k)
                    print(k, end=' ')
        q = temp


input = stdin.readline
n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visit1 = [False] * (n + 1)
visit2 = visit1.copy()
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for row in graph:
    row.sort()
dfs(v)
print()
bfs(v)
print()

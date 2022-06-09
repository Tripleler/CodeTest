# https://www.acmicpc.net/problem/24444

from sys import stdin


def bfs(i):
    global n, graph, visit, cnt
    q = [i]
    visit[i] = cnt
    cnt += 1
    while q:
        temp = list()
        for j in q:
            for k in graph[j]:
                if not visit[k]:
                    temp.append(k)
                    visit[k] = cnt
                    cnt += 1
        q = temp


input = stdin.readline
n, m, r = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visit = [0] * (n + 1)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for row in graph[1:]:
    row.sort()
cnt = 1
bfs(r)
print(*visit[1:], sep='\n')

# https://www.acmicpc.net/problem/2606

from sys import stdin


def dfs(i):
    global connect, graph, n
    for j in range(n):
        if graph[i][j] and not connect[j]:
            connect[j] = True
            dfs(j)


input = stdin.readline
n = int(input())
graph = [[False] * n for _ in range(n)]
for _ in range(int(input())):
    a, b = map(int, input().split())
    graph[a - 1][b - 1] = graph[b - 1][a - 1] = True
    connect = [False] * n
    connect[0] = True
dfs(0)
print(sum(connect) - 1)

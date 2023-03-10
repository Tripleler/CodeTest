# https://www.acmicpc.net/problem/1012

from sys import stdin


def bfs():
    global cnt, m, n, graph, r, c
    graph[r][c] = False
    q = [(r, c)]
    while q:
        temp = []
        for row, col in q:
            for a, b in move:
                if (n - 1 >= row + a >= 0) and (m - 1 >= col + b >= 0) and graph[row + a][col + b]:
                    temp.append((row + a, col + b))
                    graph[row + a][col + b] = False
        q = temp
    cnt += 1


input = stdin.readline
move = [(0, 1), (1, 0), (0, -1), (-1, 0)]
for _ in range(int(input())):
    m, n, k = map(int, input().split())
    graph = [[False] * m for _ in range(n)]
    for _ in range(k):
        c, r = map(int, input().split())
        graph[r][c] = True
    cnt = 0
    for r in range(n):
        for c in range(m):
            if graph[r][c]:
                bfs()
    print(cnt)

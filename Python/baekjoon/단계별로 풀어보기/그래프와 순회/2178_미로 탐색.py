# https://www.acmicpc.net/problem/2178

def bfs():
    global move
    q = [(0, 0)]
    graph[0][0] = 0
    cnt = 1
    while q:
        temp = []
        for r, c in q:
            for a, b in move:
                if (0 <= r + a < n) and (0 <= c + b < m) and graph[r + a][c + b]:
                    if (r + a) == (n - 1) and (c + b) == (m - 1):
                        return cnt + 1
                    graph[r + a][c + b] = 0
                    temp.append((r + a, c + b))
        q = temp
        cnt += 1


n, m = map(int, input().split())
graph = []
move = [(0, 1), (0, -1), (1, 0), (-1, 0)]
for _ in range(n):
    graph.append(list(map(int, list(input()))))
print(bfs())

# https://www.acmicpc.net/problem/2667

def bfs():
    global r, c, graph, move, cnt
    graph[r][c] = 0
    q = [(r, c)]
    house = 1
    while q:
        temp = []
        for row, col in q:
            for a, b in move:
                if (0 <= row + a < n) and (0 <= col + b < n) and graph[row + a][col + b]:
                    graph[row + a][col + b] = 0
                    temp.append((row + a, col + b))
                    house += 1
        q = temp
    cnt.append(house)


n = int(input())
graph = []
cnt = []
move = [(0, 1), (1, 0), (0, -1), (-1, 0)]
for _ in range(n):
    graph.append(list(map(int, list(input()))))
for r in range(n):
    for c in range(n):
        if graph[r][c]:
            bfs()
print(len(cnt))
print(*sorted(cnt), sep='\n')

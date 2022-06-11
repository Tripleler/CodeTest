# https://www.acmicpc.net/problem/7576

from sys import stdin


def bfs():
    global red, green, cnt
    move = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    while red:
        temp = []
        for r, c in red:
            for a, b in move:
                if (0 <= r + a < n) and (0 <= c + b < m) and (tomato[r + a][c + b] == 0):
                    tomato[r + a][c + b] = 1
                    temp.append((r + a, c + b))
                    green -= 1
        red = temp
        cnt += 1


input = stdin.readline
m, n = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(n)]
red = []
green = 0
for row in range(n):
    for col in range(m):
        if tomato[row][col] == 1:
            red.append((row, col))
        if tomato[row][col] == 0:
            green += 1
if not green:
    print(0)
else:
    cnt = 0
    bfs()
    print(-1) if green else print(cnt - 1)

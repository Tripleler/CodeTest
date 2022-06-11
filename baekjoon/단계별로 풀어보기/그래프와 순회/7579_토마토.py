# https://www.acmicpc.net/problem/7569

from sys import stdin


def bfs():
    global red, green, cnt, tomato
    move = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
    while red:
        temp = []
        for f, r, c in red:
            for z, y, x in move:
                if (0 <= f + z < h) and (0 <= r + y < n) and (0 <= c + x < m) and not tomato[f + z][r + y][c + x]:
                    tomato[f + z][r + y][c + x] = 1
                    temp.append((f + z, r + y, c + x))
                    green -= 1
        red = temp
        cnt += 1


input = stdin.readline
m, n, h = map(int, input().split())
tomato = []
for _ in range(h):
    box = []
    for _ in range(n):
        box.append(list(map(int, input().split())))
    tomato.append(box)
red = []
green = 0
for floor in range(h):
    for row in range(n):
        for col in range(m):
            if tomato[floor][row][col] == 1:
                red.append((floor, row, col))
            if not tomato[floor][row][col]:
                green += 1
if not green:
    print(0)
else:
    cnt = 0
    bfs()
    print(-1) if green else print(cnt - 1)

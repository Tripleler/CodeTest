# https://www.acmicpc.net/problem/7562

from sys import stdin


def bfs():
    global x, y
    q = [(a, b)]
    cnt = 0
    while q:
        temp = []
        for row, col in q:
            for r, c in move:
                if (0 <= row + r < l) and (0 <= col + c < l) and not chess[row + r][col + c]:
                    if row + r == x and col + c == y:
                        return cnt + 1
                    else:
                        chess[row + r][col + c] = True
                        temp.append((row + r, col + c))
        cnt += 1
        q = temp


input = stdin.readline
for _ in range(int(input())):
    l = int(input())
    a, b = map(int, input().split())
    x, y = map(int, input().split())
    dx = abs(x - a)
    dy = abs(y - b)
    if not dx + dy:
        print(0)
    elif dx == dy == 2:
        print(4)
    else:
        chess = [[False] * l for _ in range(l)]
        chess[a][b] = True
        move = [(2, 1), (2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2), (-2, 1), (-2, -1)]
        print(bfs())

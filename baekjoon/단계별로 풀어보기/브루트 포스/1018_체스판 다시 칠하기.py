# https://www.acmicpc.net/problem/1018

n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(input()))
chessB = ['B' if i % 2 else 'W' for i in range(8)]
chessW = ['W' if i % 2 else 'B' for i in range(8)]
chess1 = [chessB if i % 2 else chessW for i in range(8)]
chess2 = [chessW if i % 2 else chessB for i in range(8)]
cnt = []
for i in range(n - 7):
    for j in range(m - 7):
        cnt1 = 0
        cnt2 = 0
        for r in range(i, i + 8):
            for c in range(j, j + 8):
                if board[r][c] != chess1[r - i][c - j]:
                    cnt1 += 1
                if board[r][c] != chess2[r - i][c - j]:
                    cnt2 += 1
        cnt.append(min(cnt1, cnt2))
print(min(cnt))

# https://www.acmicpc.net/problem/16928

def bfs():
    global board, visit
    i = 1
    cnt = 1
    roll = [1, 2, 3, 4, 5, 6]
    q = []
    for x in roll:
        visit[i + x] = True
        q.append(board[i + x])
    while q:
        temp = []
        for loc in q:
            for x in roll:
                if loc + x == 100:
                    return cnt
                if loc + x < 100 and not visit[loc + x]:
                    temp.append(board[loc + x])
                    visit[loc + x] = True
        q = temp
        cnt += 1


n, m = map(int, input().split())
board = [x for x in range(101)]
visit = [False] * 100
for _ in range(m + n):
    a, b = map(int, input().split())
    board[a] = b
print(bfs() + 1)

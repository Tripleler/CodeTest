# def check(ad, co):
#     if len(ad) == 3:
#         ad = '0b00' + ad[-1]
#     elif len(ad) == 4:
#         ad = '0b0' + ad[-2:]
#     if co == 'R':
#         print(1 if int(ad[2]) else 0)
#     if co == 'W':
#         print(1 if int(ad[3]) else 0)
#     if co == 'X':
#         print(1 if int(ad[4]) else 0)
#
#
# u, f = map(int, input().split())
# group = {}
# for _ in range(u):
#     s = input().split()
#     if len(s) == 2:  # 그룹에 속해있다면 {이름:그룹명리스트}
#         group[s[0]] = s[1].split(',')
# dic = {}
# for _ in range(f):  # {파일명 : {admin:admin, u_name:u_name, g_name:g_name}}
#     f_name, admin, u_name, g_name = input().split()
#     f_dic = {
#         'admin': admin,
#         'user_name': u_name,
#         'group_name': g_name
#     }
#     dic[f_name] = f_dic
# for _ in range(int(input())):
#     u_name, f_name, cond = input().split()
#     f_name = dic[f_name]
#     if u_name == f_name['user_name']:  # 파일명의 u_name 과 요청자명이 같으면
#         admin = bin(int(f_name['admin'][0]))
#         check(admin, cond)
#     elif (u_name == f_name['group_name']) or (u_name in group.keys() and f_name['group_name'] in group[u_name]):
#         # 파일명의 g_name 과 요청자명이 같거나 혹은 (요청자명이 파일명의 g_name 에 속하면)
#         admin = bin(int(f_name['admin'][1]))
#         check(admin, cond)
#     else:  # other
#         admin = bin(int(f_name['admin'][2]))
#         check(admin, cond)


# from collections import deque
#
#
# def check(sudoku, t):
#     rows = sudoku[t[0]]
#     cols = [x[t[1]] for x in sudoku]
#     square = []
#     for i in range(t[0] // 3 * 3, t[0] // 3 * 3 + 3):
#         for j in range(t[1] // 3 * 3, t[1] // 3 * 3 + 3):
#             square.append(sudoku[i][j])
#     a = set(range(1, 10)).difference(rows)
#     b = set(range(1, 10)).difference(cols)
#     c = set(range(1, 10)).difference(square)
#     union = []
#     for i in range(1, 10):
#         if (i in a) & (i in b) & (i in c):
#             union.append(i)
#     return union[0] if len(union) == 1 else False
#
#
# sudoku = []
# for _ in range(9):
#     sudoku.append(list(map(int, input().split())))
# problem = deque()
# for row in range(9):
#     for col in range(9):
#         if not sudoku[row][col]:
#             problem.append(tuple((row, col)))
# while len(problem):
#     p = problem[-1]
#     solve = check(sudoku, p)
#     if solve:
#         sudoku[p[0]][p[1]] = solve
#         problem.pop()
#     else:
#         problem.rotate()
# for row in range(9):
#     print(*sudoku[row])


# from collections import deque
# import sys
# read = sys.stdin.readline
#
# def bfs(v):
#     q = deque()
#     q.append(v)
#     visit_list[v] = 1
#     while q:
#         print(q)
#         v = q.popleft()
#         print(v)
#         for i in range(1, n + 1):
#             print(visit_list)
#             if visit_list[i] == 0 and graph[v][i] == 1:
#                 q.append(i)
#                 visit_list[i] = 1
#
# n, m, v = map(int, read().split())
#
# graph = [[0] * (n + 1) for _ in range(n + 1)]
# visit_list = [0] * (n + 1)
# visit_list2 = [0] * (n + 1)
#
# for _ in range(m):
#     a, b = map(int, read().split())
#     graph[a][b] = graph[b][a] = 1
#
# print(graph)
# bfs(v)

# n = 9
# s = '***\n* *\n***'
# i = 1
# while n > 1:
#     space = '   ' * i
#     size = (len(s) - 2) // 3
#     l = []
#     i = 0
#     for _ in range(3):
#         l.append(s[i: i + size])
#         i += size + 1
#     print(l)
#     s = [l[0] * 3, l[1] * 3, l[2] * 3, l[0] + space + l[0], l[1] + space + l[1], l[2] + space + l[2], l[0] * 3, l[1] * 3, l[2] * 3]
#     s = '\n'.join(s)
#     i *= 3
#     n //= 3
# print(s)

def n_and_m(depth, n, m):
    if depth == m:
        print(' '.join(map(str, answer)))

    for i in range(1, n + 1):
        print(visited)
        if not visited[i]:
            visited[i] = True
            answer.append(i)
            n_and_m(depth + 1, n, m)
            visited[i] = False
            answer.pop()


n, m = map(int, input().split())
visited = [False] * (n + 1)
answer = []

n_and_m(0, n, m)

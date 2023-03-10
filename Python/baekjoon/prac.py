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

# def n_and_m(depth, n, m):
#     if depth == m:
#         print(' '.join(map(str, answer)))
#
#     for i in range(1, n + 1):
#         print(visited)
#         if not visited[i]:
#             visited[i] = True
#             answer.append(i)
#             n_and_m(depth + 1, n, m)
#             visited[i] = False
#             answer.pop()
#
#
# n, m = map(int, input().split())
# visited = [False] * (n + 1)
# answer = []
#
# n_and_m(0, n, m)

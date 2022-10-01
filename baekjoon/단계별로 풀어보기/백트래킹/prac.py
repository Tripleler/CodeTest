# https://www.acmicpc.net/problem/2580
# 모든 자리가 0일때 채우는법도 구현해야함... 백트래킹어렵네

def check(sudoku, t):
    # check row
    rows = sudoku[t[0]]
    a = set(range(1, 10)).difference(rows)
    if len(a) == 1:
        return a.pop()

    # check column
    cols = [x[t[1]] for x in sudoku]
    b = set(range(1, 10)).difference(cols)
    if len(b) == 1:
        return b.pop()

    # check 3X3 square
    square = []
    for i in range(t[0] // 3 * 3, t[0] // 3 * 3 + 3):
        for j in range(t[1] // 3 * 3, t[1] // 3 * 3 + 3):
            square.append(sudoku[i][j])
    c = set(range(1, 10)).difference(square)
    if len(c) == 1:
        return c.pop()

    return False


sudoku = [list(map(int, input().split())) for _ in range(9)]
problem = []
for row in range(9):
    for col in range(9):
        if not sudoku[row][col]:
            problem.append(tuple((row, col)))
while len(problem):
    p = problem.pop(0)
    solve = check(sudoku, p)
    if solve:
        sudoku[p[0]][p[1]] = solve
    else:
        problem.append(p)
for row in range(9):
    print(*sudoku[row])

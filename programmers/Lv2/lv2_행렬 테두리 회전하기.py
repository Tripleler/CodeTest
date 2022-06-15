# https://programmers.co.kr/learn/courses/30/lessons/77485?language=python3

def solution(rows, columns, queries):
    answer = []
    square = []
    for j in range(rows):
        a = []
        for i in range(1 + columns * j, columns + 1 + columns * j):
            a.append(i)
        square.append(a)
    for i in range(len(queries)):
        check = []
        a = square[queries[i][0] - 1][queries[i][3] - 1]
        c = square[queries[i][2] - 1][queries[i][1] - 1]
        for j in range(queries[i][3] - queries[i][1]):
            square[queries[i][0] - 1][queries[i][3] - 1 - j] = square[queries[i][0] - 1][queries[i][3] - 1 - j - 1]
            square[queries[i][2] - 1][queries[i][1] - 1 + j] = square[queries[i][2] - 1][queries[i][1] - 1 + j + 1]
            check.append(square[queries[i][0] - 1][queries[i][3] - 1 - j - 1])
            check.append(square[queries[i][2] - 1][queries[i][1] - 1 + j + 1])
        for k in range(queries[i][2] - queries[i][0] - 1):
            square[queries[i][2] - 1 - k][queries[i][3] - 1] = square[queries[i][2] - 1 - k - 1][queries[i][3] - 1]
            square[queries[i][0] - 1 + k][queries[i][1] - 1] = square[queries[i][0] - 1 + k + 1][queries[i][1] - 1]
            check.append(square[queries[i][2] - 1 - k - 1][queries[i][3] - 1])
            check.append(square[queries[i][0] - 1 + k + 1][queries[i][1] - 1])
        square[queries[i][0] - 1 + 1][queries[i][3] - 1] = a
        square[queries[i][2] - 1 - 1][queries[i][1] - 1] = c
        check.append(a)
        check.append(c)
        answer.append(min(check))
    return answer


print(solution(6, 6, [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]))
print(solution(3, 3, [[1, 1, 2, 2], [1, 2, 2, 3], [2, 1, 3, 2], [2, 2, 3, 3]]))
print(solution(100, 97, [[1, 1, 100, 97]]))

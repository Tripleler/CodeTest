def solution(line):
    answer = []
    x_list = []
    y_list = []
    from itertools import combinations
    for i in combinations(line, 2):
        a = i[0][0]
        b = i[0][1]
        c = i[1][0]
        d = i[1][1]
        e = i[0][2]
        f = i[1][2]
        if a * d == b * c:
            pass
        else:
            x = (b * f - e * d) / (a * d - b * c)
            y = (e * c - a * f) / (a * d - b * c)
            if (int(x) != x) | (int(y) != y):
                pass
            else:
                x_list.append(int(x))
                y_list.append(-int(y))
    x_list = [x - min(x_list) for x in x_list]
    y_list = [y - min(y_list) for y in y_list]
    cordinate = [(x, y) for x, y in zip(x_list, y_list)]
    for i in range(max(y_list) - min(y_list) + 1):
        point = ''
        for j in range(max(x_list) - min(x_list) + 1):
            if (j, i) in cordinate:
                point += '*'
            else:
                point += '.'
        answer.append(point)
    return answer


print(solution([[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]))
print(solution([[0, 1, -1], [1, 0, -1], [1, 0, 1]]))
print(solution([[1, -1, 0], [2, -1, 0]]))
print(solution([[1, -1, 0], [2, -1, 0], [4, -1, 0]]))

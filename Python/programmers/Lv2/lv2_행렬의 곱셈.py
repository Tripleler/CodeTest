def solution(arr1, arr2):
    answer = []
    for k in range(len(arr1)):
        row = []
        for j in range(len(arr2[0])):
            factor = 0
            for i in range(len(arr1[0])):
                factor += (arr1[k][i] * arr2[i][j])
            row.append(factor)
        answer.append(row)
    return answer


print(solution([[1, 4], [3, 2], [4, 1]], [[3, 3], [3, 3]]))
print(solution([[2, 3, 2], [4, 2, 4], [3, 1, 4]], [[5, 4, 3], [2, 4, 1], [3, 1, 1]]))

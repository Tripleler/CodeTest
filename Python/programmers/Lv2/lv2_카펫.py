def solution(brown, yellow):
    li = []
    answer = []
    for i in range(1, round(yellow ** 0.5) + 1):
        if yellow % i == 0:
            li.append([i, int(yellow / i)])
    for j in li:
        if (j[0] + 2) * (j[1] + 2) == brown + yellow:
            answer.append(j[1] + 2)
            answer.append(j[0] + 2)
            break
    return answer


print(solution(10, 2))
print(solution(8, 1))
print(solution(24, 24))

def solution(n, left, right):
    answer = []
    for i in range(left // n, right // n + 1):
        for j in range(1, n + 1):
            if i + 1 <= j:
                answer.append(j)
            else:
                answer.append(i + 1)
    if (right + 1) % n == 0:
        answer = answer[left % n:]
    else:
        answer = answer[left % n:-(n - right % n - 1)]
    return answer


print(solution(3, 2, 5))
print(solution(4, 7, 14))

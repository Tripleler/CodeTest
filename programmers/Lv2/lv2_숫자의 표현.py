def solution(n):
    answer = 1
    for i in range(1, n // 2 + 1):
        if (n % (2 * i + 1) == 0) & (n >= (2 * i ** 2 + 3 * i + 1)):
            answer += 1
        if (n % (2 * i) == i) & (n > (2 * i ** 2 + i)):
            answer += 1
    return answer


print(solution(15))

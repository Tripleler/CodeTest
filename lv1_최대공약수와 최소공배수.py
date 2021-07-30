def solution(n, m):
    answer = []
    for i in range(min(n, m), 0, -1):
        if (min(n, m) % i == 0) & (max(n, m) % i == 0):
            answer.append(i)
            break
    answer.append(int(n * m / i))
    return answer
print(solution(2,5))
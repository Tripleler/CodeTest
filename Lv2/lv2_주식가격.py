def solution(prices):
    answer = []
    for i in range(len(prices) - 1):
        for j in range(len(prices) - i):
            if prices[i] > prices[i + j]:
                break
        answer.append(j)
    answer.append(0)
    return answer


print(solution([1, 2, 3, 2, 3]))

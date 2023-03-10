def solution(arr):
    answer = arr[0]
    if len(arr) == 1:
        return answer
    for i in range(len(arr) - 1):
        for j in range(min(answer, arr[i + 1]), 0, -1):
            if (answer % j == 0) & (arr[i + 1] % j == 0):
                answer = int(answer * arr[i + 1] / j)
                break
    return answer


print(solution([2, 6, 8, 14]), solution([1, 2, 3]))
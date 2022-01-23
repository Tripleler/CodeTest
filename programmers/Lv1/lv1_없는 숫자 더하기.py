def solution(numbers):
    answer = sum({0, 1, 2, 3, 4, 5, 6, 7, 8, 9} - set(numbers))
    return answer


print(solution([1, 2, 3, 4, 6, 7, 8, 0]))
print(solution([5, 8, 4, 0, 6, 7, 9]))

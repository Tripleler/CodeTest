def solution(n):
    a, b = 0, 1
    while n > 1:
        a, b = b, a + b
        n -= 1
    return b % 1234567


print(solution(3), solution(5))

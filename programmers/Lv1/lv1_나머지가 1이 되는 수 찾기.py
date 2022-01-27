def solution(n):
    num = n - 1
    for i in range(2, round(num**0.5)):
        if num % i == 0:
            return i
    return n - 1

# https://programmers.co.kr/learn/courses/30/lessons/12985?language=python3

def solution(n, a, b):
    answer = 1
    A = min(a, b)
    B = max(a, b)
    while (B % 2 != 0) | (B - 1 != A):
        A = round(A / 2 + 0.1)
        B = round(B / 2 + 0.1)
        answer += 1
    return answer


print(solution(8, 4, 7))

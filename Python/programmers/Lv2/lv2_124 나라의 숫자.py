# https://school.programmers.co.kr/learn/courses/30/lessons/12899?language=python3

def solution(n):
    num = 3
    answer = ''
    while n > 0:
        n, mod = divmod(n, num)
        if mod == 0:
            answer += '4'
            n = n - 1
        else:
            answer += str(mod)
    answer = answer[::-1]
    return answer


print(solution(1))
print(solution(2))
print(solution(3))
print(solution(4))

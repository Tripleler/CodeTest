def solution(s):
    cnt = 0
    pop = 0
    while s != '1':
        pop += s.count('0')
        cnt += 1
        s = bin(s.count('1'))[2:]
    answer = [cnt, pop]
    return answer


print(solution("110010101001"))
print(solution("01110"))
print(solution("1111111"))

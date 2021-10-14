def solution(s):
    answer = ''
    li1 = s.split()
    li2 = []
    for i in li1:
        li2.append(int(i))
    answer += str(min(li2))
    answer += ' '
    answer += str(max(li2))
    return answer


print(solution("1 2 3 4"), solution("-1 -2 -3 -4"), solution("-1 -1"))

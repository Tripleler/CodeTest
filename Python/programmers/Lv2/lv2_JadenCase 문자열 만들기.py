def solution(s):
    answer = ''
    s = s.lower()
    li = s.split(' ')
    for i in li:
        if i == '':
            answer += ' '
        else:
            answer += i[0].upper()
            if len(i) >= 2:
                answer += i[1:]
            answer += ' '
    answer = answer[:-1]
    return answer


print(solution("3people unFollowed me"))
print(solution("for the last week"))

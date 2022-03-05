# https://programmers.co.kr/learn/courses/30/lessons/76502?language=python3

import re


def solution(s):
    answer = 0
    for i in range(len(s)):
        s = s[1:] + s[0]
        s2 = s
        while ('()' in s2) | ('{}' in s2) | ('[]' in s2):
            s2 = re.sub('(\(\))|(\{\})|(\[\])', '', s2)
        if s2 == '':
            answer += 1
    return answer


print(solution("[](){}"))
print(solution("}]()[{"))
print(solution("[)(]"))
print(solution("}}}"))

# https://programmers.co.kr/learn/courses/30/lessons/64065?language=python3

import re


def solution(s):
    answer = []
    p = re.compile('\d+')
    s = s.split('}')[:-2]
    li = []
    for i in s:
        li.append(p.findall(i))
    li.sort(key=len)
    for i in range(len(li)):
        answer.append(list(set(li[i]) - set(answer))[0])
    answer = [int(x) for x in answer]
    return answer


print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))
print(solution("{{20,111},{111}}"))
print(solution("{{123}}"))
print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))

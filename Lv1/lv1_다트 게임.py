import re


def solution(dartResult):
    p = re.compile('(\d+)([SDT])([*#]?)')
    li = p.findall(dartResult)
    answer = []
    for i in range(len(li)):
        a = int(li[i][0])
        if li[i][1] == 'T':
            a **= 3
        if li[i][1] == 'D':
            a **= 2
        if li[i][2] == '#':
            a *= -1
        answer.append(a)
        if li[i][2] == '*':
            if i == 0:
                answer[0] *= 2
            else:
                answer[i - 1] *= 2
                answer[i] *= 2
    answer = sum(answer)
    return answer


print(solution("1S2D*3T"))
print(solution("1D2S#10S"))
print(solution("1D2S0T"))
print(solution("1S*2T*3S"))
print(solution("1D#2S*3S"))
print(solution("1T2D3D#"))
print(solution("1D2S3T*"))

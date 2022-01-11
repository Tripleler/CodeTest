import re


def solution(str1, str2):
    p = re.compile('[a-z]{2}')
    str1 = str1.lower()
    str2 = str2.lower()
    li1 = []
    li2 = []
    for i in range(len(str1) - 1):
        if p.match(str1[i:i + 2]):
            li1.append(str1[i:i + 2])
    for i in range(len(str2) - 1):
        if p.match(str2[i:i + 2]):
            li2.append(str2[i:i + 2])
    l = 0
    m = 0
    for i in set(li1):
        l += min(li1.count(i), li2.count(i))
    for i in set(li1 + li2):
        m += max(li1.count(i), li2.count(i))
    if m == 0:
        answer = 65536
    else:
        answer = int((l / m * 65536))
    return answer


print(solution('FRANCE', 'french'))
print(solution('handshake', 'shake hands'))
print(solution('aa1+aa2', 'AAAA12'))
print(solution('E=M*C^2', 'e=m*c^2'))

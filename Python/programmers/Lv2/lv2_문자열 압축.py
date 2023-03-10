# https://programmers.co.kr/learn/courses/30/lessons/60057?language=python3

def solution(s):
    answer = []
    for i in range(1, len(s) // 2 + 1):
        st = ''
        num = len(s)
        cnt = 0
        for j in range(0, len(s), i):
            if st != s[j:j + i]:
                st = s[j:j + i]
                if cnt:
                    num += len(str(cnt + 1))
                    num -= (cnt * i)
                    cnt = 0
            else:
                cnt += 1
        if cnt:
            num += len(str(cnt + 1))
            num -= (cnt * i)
        answer.append(num)
    return min(answer) if answer else 1

print(solution("aabbaccc"))
print(solution("ababcdcdababcdcd"))
print(solution("abcabcdede"))
print(solution("abcabcabcabcdededededede"))
print(solution("xababcdcdababcdcd"))
print(solution("a"))

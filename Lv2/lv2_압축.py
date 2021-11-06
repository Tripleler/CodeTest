def solution(msg):
    answer = []
    dic = {}
    for i in range(65, 91):
        dic[chr(i)] = i - 64
    i = 0
    num = 27
    while i < len(msg):
        for j in range(len(msg), 0, -1):
            try:
                answer.append(dic[msg[i:j]])
                dic[msg[i:j + 1]] = num
                num += 1
                i += (j - i)
            except:
                pass
    return answer


print(solution('KAKAO'))
print(solution('TOBEORNOTTOBEORTOBEORNOT'))
print(solution('ABABABABABABABAB'))

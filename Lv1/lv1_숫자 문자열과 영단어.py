def solution(s):
    dic = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7',
           'eight': '8', 'nine': '9'}
    side = 0
    li = []
    while True:
        try:
            int(s[side:side + 1])
            li.append(s[side:side + 1])
            side += 1
            if side == len(s):
                break
        except:
            for i in range(3, 6):
                if s[side:side + i] in dic:
                    li.append(dic[s[side:side + i]])
                    side += i
                    break
            if side == len(s):
                break
    answer = int("".join(li))
    return answer


print(solution("one4seveneight"))
print(solution("23four5six7"))
print(solution("2three45sixseven"))
print(solution("123"))

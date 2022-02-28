# https://programmers.co.kr/learn/courses/30/lessons/77885?language=python3

from collections import Counter


def solution(numbers):
    answer = []
    for i in numbers:
        i = int(i)
        if Counter(bin(i))['0'] == 1:
            answer.append(int((i + 1) * 1.5) - 1)
        elif bin(i)[-1] == '0' or bin(i)[-2] == '0':
            answer.append(i + 1)
        else:
            n = bin(i).rfind('0')
            li = list(bin(i))
            li[n] = '1'
            li[n + 1] = '0'
            answer.append(int(''.join(li), 2))
    return answer


print(solution([x for x in range(32)] + [43]))

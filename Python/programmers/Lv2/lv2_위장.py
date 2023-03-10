# https://programmers.co.kr/learn/courses/30/lessons/42578?language=python3

from collections import Counter


def solution(clothes):
    answer = 1
    dic = Counter([x[1] for x in clothes]).values()
    for i in dic:
        answer *= (i+1)
    answer -= 1
    return answer


print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))
print(solution([["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]))

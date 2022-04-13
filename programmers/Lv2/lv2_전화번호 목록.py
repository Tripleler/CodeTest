# https://programmers.co.kr/learn/courses/30/lessons/42577?language=python3

def solution(phone_book):
    length = set([len(x) for x in phone_book])
    for i in length:
        set1 = set([x for x in phone_book if len(x) == i])
        set2 = set([x[:i] for x in phone_book if len(x) > i])
        if (set1 - set2) != set1:
            return False
    return True

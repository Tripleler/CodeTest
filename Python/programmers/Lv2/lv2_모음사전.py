def solution(word):
    from itertools import product
    p = ['A', 'E', 'I', 'O', 'U']
    dic = []
    for i in range(1, 6):
        dic += list(product(p, repeat=i))
    dic.sort()
    answer = dic.index(tuple(word)) + 1
    return answer


print(solution("AAAAE"))
print(solution("AAAE"))
print(solution("I"))
print(solution("EIO"))

# https://programmers.co.kr/learn/courses/30/lessons/42747?language=python3

def solution(citations):
    citations.sort(reverse=True)  # 정렬
    if not max(citations):  # 0만 이루어졌다면
        return 0  # H-index는 0
    else:
        for i, h in enumerate(citations, start=1):
            if h < i:
                i -= 1  # 다음 i에서 아닌걸 알았으므로 1 빼기
                break
        return i


print(solution([3, 0, 6, 1, 5]))  # 3
print(solution([10, 10, 10, 10, 10]))  # 5
print(solution([0, 0, 0, 0, 0]))  # 0
print(solution([1, 1, 1, 10]))  # 1
print(solution([9, 7, 6, 2, 1]))  # 3
print(solution([0, 0, 0, 0, 1]))  # 1

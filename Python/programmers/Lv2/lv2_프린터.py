# https://programmers.co.kr/learn/courses/30/lessons/42587?language=python3

def solution(priorities, location):
    idx = [i for i in range(len(priorities))]
    answer = 0
    while True:
        priority = priorities.pop(0)
        n = idx.pop(0)
        if len(priorities):
            if priority < max(priorities):
                priorities.append(priority)
                idx.append(n)
            else:
                answer += 1
                if n == location:
                    break
        else:
            return answer + 1
    return answer


print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 1))

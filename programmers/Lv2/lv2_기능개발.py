# https://programmers.co.kr/learn/courses/30/lessons/42586?language=python3

def solution(progresses, speeds):
    day = []
    answer = [1]
    for i, j in zip(progresses, speeds):
        day.append((100 - i) // j + ((100 - i) % j != 0))
    x = day.pop(0)
    while day:
        y = day.pop(0)
        if y <= x:
            answer[-1] += 1
        else:
            answer.append(1)
            x = y
    return answer


print(solution([93, 30, 55], [1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))

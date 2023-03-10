# https://programmers.co.kr/learn/courses/30/lessons/42885?language=python3

def solution(people, limit):
    answer = 0
    people.sort(reverse=True)
    i = 0
    j = len(people) - 1
    while i < j:
        if people[i] + people[j] <= limit:
            j -= 1
        i += 1
        answer += 1
    if i == j:
        return answer + 1
    else:
        return answer


print(solution([70, 50, 80, 50], 100))
print(solution([70, 80, 50], 100))

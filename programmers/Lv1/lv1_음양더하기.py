def solution(absolutes, signs):
    answer = 0
    for i in range(len(absolutes)):
        answer += absolutes[i] * list(map(lambda x: 1 if x == True else -1, signs))[i]
    return answer

print(solution([4,7,12], [True, False, True]))
print(solution([1,2,3], [False, False, True]))
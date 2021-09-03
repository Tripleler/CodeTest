def solution(seoul):
    for i, j in enumerate(seoul):
        if j == 'Kim':
            s=i
            break
    answer = f'김서방은 {s}에 있다'
    return answer
print(solution(["Jane", "Kim"]))
def solution(n):
    li=sorted(str(n), reverse=True)
    answer = int(''.join(li))
    return answer
print(solution(118372))
def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    lost2 = []
    for i in reserve:
        if i in lost:
            lost.remove(i)
            lost2.append(i)
    reserve2 = [x for x in reserve if x not in lost2]
    for i in reserve2:
        if i-1 in lost:
            lost.remove(i-1)
        elif i+1 in lost:
            lost.remove(i+1)
    answer = n-len(lost)
    return answer

print(solution(5, [2,4], [1,3,5]))
print(solution(5, [2,4], [3]))
print(solution(3, [3], [1]))
import itertools
def solution(nums):
    answer = 0
    n = max(nums)*3
    li = [True for x in range(n)]
    li[0] = False
    for i in range(n):
        if li[i] == True:
            x = n//(i+1)
            for j in range(x-1):
                li[(i+1)*(j+2)-1] = False
    number = [x+1 for x in range(n) if li[x] == True]
    li2 = [sum(x) for x in list(itertools.combinations(nums, 3))]
    for j in li2:
        if j in number:
            answer += 1
    return answer
print(solution([1,2,3,4]), solution([1,2,7,6,4]))
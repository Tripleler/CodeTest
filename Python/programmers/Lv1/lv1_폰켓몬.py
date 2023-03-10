def solution(nums):
    l = int(len(nums)/2)
    s = len(set(nums))
    answer = min(s,l)
    return answer
print(solution([3,1,2,3]), solution([3,3,3,2,2,4]), solution([3,3,3,2,2,2]))
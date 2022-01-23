def solution(arr):
    if len(arr)==1:
        arr=[-1]
    else:
        arr.remove(min(arr))
    return arr
print(solution([4,3,2,1]))
print(solution([10]))
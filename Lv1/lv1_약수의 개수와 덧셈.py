def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        num=0
        for j in range(1,int((i+2)/2)):
            if i%j==0:
                num+=1
        if num%2==0:
            answer-=i
        else:
            answer+=i
    return answer
print(solution(13,17), solution(24,27))
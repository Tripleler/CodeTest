def solution(price, money, count):
    cnt=0
    for i in range(1,count+1):
        cnt+=i
    answer=cnt*price-money if cnt*price-money>0 else 0
    return answer
print(solution(3,20,4))

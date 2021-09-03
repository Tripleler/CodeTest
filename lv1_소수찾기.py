def solution(n):
    li=[]
    for i in range(n):
        li.append(True)
    li[0]=False
    for j in range(n):
        if li[j]==False:
            pass
        else:
            x=n//(j+1)
            for k in range(x-1):
                li[(j+1)*(k+2)-1]=False
    return sum(li)
print(solution(10), solution(5))
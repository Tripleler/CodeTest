def solution(N, stages):
    li1=[]
    li2=[]
    answer=[]
    s=len(stages)
    for i in range(1, N+2):
        li1.append(stages.count(i))
    li2.append(li1[0]/(s))
    for j in range(1,N):
        if li1[j]==0:
            li2.append(0)
            s-=li1[j-1]
        else:
            li2.append(li1[j]/(s-li1[j-1]))
            s-=li1[j-1]

    dictionary = {i+1 : string for i,string in enumerate(li2)}

    for key, value in sorted(dictionary.items(),key= lambda dictionary: dictionary[1], reverse=True):
        answer.append(key)
    return answer
print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4,4,4,4,4]))

def solution(arr1, arr2):
    answer=[]
    answer2=[]
    for i in range(len(arr1)):
        for j in range(len(arr1[i])):
            answer2.append(arr1[i][j]+arr2[i][j])
        answer.append(answer2)
        answer2=[]
    return answer
print(solution([[1,2],[2,3]],[[3,4],[5,6]]))

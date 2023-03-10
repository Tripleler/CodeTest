def solution(n, arr1, arr2):
    answer = []
    a=arr1+arr2
    b=[]
    for i in range(2*n):
        if len(bin(a[i])[2:])<n:
            b.append((n-len(bin(a[i])[2:]))*'0'+bin(a[i])[2:])
        else:
            b.append(bin(a[i])[2:])
    arr1=b[0:n]
    arr2=b[n:2*n]
    for i, j in zip(arr1, arr2):
        c=''
        for k in range(n):
            if (i[k]=='0')&(j[k]=='0'):
                c+=' '
            else:
                c+='#'
        answer.append(c)
    return answer
print(solution(5,[9, 20, 28, 18, 11],[30, 1, 21, 17, 28]))
print(solution(6,[46, 33, 33 ,22, 31, 50],[27 ,56, 19, 14, 14, 10]))
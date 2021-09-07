def solution(s):
    answer = ''
    li=[]
    for i in s:
        li.append(i)
    li.sort(reverse=True)
    return ''.join(li)
print(solution("Zbcdefg"))
def solution(s):
    answer = ''
    if len(s)%2==1:
        answer=(s[int((len(s)-1)/2)])
    else:
        answer=(s[int(len(s)/2)-1:int(len(s)/2)+1])
    return answer
print(solution("abcde"), solution("qwer"))
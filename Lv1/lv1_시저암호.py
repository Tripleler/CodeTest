import string
dic={}
for i in range(len(string.ascii_lowercase)):
    dic[string.ascii_lowercase[i]] = i
    dic[string.ascii_uppercase[i]] = i + 100
dic[' ']=' '
def solution(s, n):
    answer=''
    li=[]
    for i in range(len(s)):
        if dic[s[i]] != ' ':
            if (70>=dic[s[i]]+n>=26)|(170>=dic[s[i]]+n>=126):
                li.append(dic[s[i]]+n-26)
            else:
                li.append(dic[s[i]]+n)
        else:
            li.append(' ')
    for i in li:
        for j in dic:
            if dic[j]==i:
                answer+=j
    return answer
print(solution('AB', 1))
print(solution('z', 1))
print(solution('a B z', 4))
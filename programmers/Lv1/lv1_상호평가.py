def solution(scores):
    answer=''
    for i in range(len(scores)):
        score=[]
        for j in range(len(scores)):
            score.append(scores[j][i])
        score.sort()
        score_sum = sum(score)
        if (scores[i][i]==score[0] & scores[i][i]!=score[1])|(scores[i][i]==score[-1] & scores[i][i]!=score[-2]):
            score_sum-=scores[i][i]
            score_mean = score_sum/(len(scores)-1)
        else:
            score_mean = score_sum/len(scores)
        if score_mean >= 90:
            answer+='A'
        elif score_mean >= 80:
            answer+='B'
        elif score_mean >= 70:
            answer+='C'
        elif score_mean >= 50:
            answer+='D'
        else:
            answer+='F'
    return answer
print(solution([[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]]))
print(solution([[50,90],[50,87]]))
print(solution([[70,49,90],[68,50,38],[73,31,100]]))
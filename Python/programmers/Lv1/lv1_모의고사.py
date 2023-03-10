def solution(answers):
    stu1=[]
    stu2=[]
    stu3=[]
    answer=[0,0,0]
    answer2=[]
    for i in range(len(answers)):
        if i%5==0:
            stu1.append(1)
        elif i%5==1:
            stu1.append(2)
        elif i%5==2:
            stu1.append(3)
        elif i%5==3:
            stu1.append(4)
        else:
            stu1.append(5)
    for i in range(len(answers)):
        if i%2==0:
            stu2.append(2)
        elif i%8==1:
            stu2.append(1)
        elif i%8==3:
            stu2.append(3)
        elif i%8==5:
            stu2.append(4)
        else:
            stu2.append(5)
    for i in range(len(answers)):
        if (i%10==0)|(i%10==1):
            stu3.append(3)
        elif (i%10==2)|(i%10==3):
            stu3.append(1)
        elif (i%10==4)|(i%10==5):
            stu3.append(2)
        elif (i%10==6)|(i%10==7):
            stu3.append(4)
        else:
            stu3.append(5)
    for i in range(len(answers)):
        if answers[i]==stu1[i]:
            answer[0]+=1
        if answers[i]==stu2[i]:
            answer[1]+=1
        if answers[i]==stu3[i]:
            answer[2]+=1
    if answer[0]==max(answer):
        answer2.append(1)
    if answer[1]==max(answer):
        answer2.append(2)
    if answer[2]==max(answer):
        answer2.append(3)
    return answer2

print(solution([1,2,3,4,5]), solution([1,3,2,4,2]))
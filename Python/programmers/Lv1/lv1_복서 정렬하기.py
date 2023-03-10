import pandas as pd
def solution(weights, head2head):
    answer = []
    winper=[]
    heavy=[]
    for i in range(len(head2head)):
        W=0
        L=0
        H=0
        for j in range(len(head2head[i])):
            if head2head[i][j] == 'W':
                W+=1
                if weights[i]<weights[j]:
                    H+=1
            elif head2head[i][j] == 'L':
                L+=1
        if W+L==0:
            winper.append(0)
        else:
            winper.append(W/(W+L))
        heavy.append(H)
    df=pd.DataFrame(columns=['weights','winper', 'heavy'])
    df.weights=weights
    df.winper=winper
    df.heavy=heavy
    df.reset_index(inplace=True)
    df=df.sort_values(by=['winper', 'heavy', 'weights','index'], ascending=[False, False, False, True])
    for i in df['index']:
        answer.append(i+1)
    return answer
print(solution([50,82,75,120],["NLWL","WNLL","LWNW","WWLN"]))
print(solution([145,92,86],["NLW","WNL","LWN"]))
print(solution([60,70,60],	["NNN","NNN","NNN"]))
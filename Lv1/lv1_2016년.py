def solution(a, b):
    num=0
    day=['SUN','MON','TUE','WED','THU','FRI','SAT']
    li=[31,29,31,30,31,30,31,31,30,31,30,31]
    for i in range(a):
        num+=li[i]
    num=num-li[a-1]+b+4
    answer=day[num%7]
    return answer
print(solution(5,24))
def solution(x):
    n=0
    s=str(x)
    for i in s:
        n+=int(i)
    return x%n==0
print(solution(10))
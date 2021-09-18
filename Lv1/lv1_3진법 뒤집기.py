def solution(n):
    answer = 0
    three=''
    while n>0:
        n, mod = divmod(n,3)
        three+=str(mod)
    for i, j in zip(range(len(three)), three[::-1]):
        answer+=3**i*int(j)
    return answer
print(solution(45), solution(125))
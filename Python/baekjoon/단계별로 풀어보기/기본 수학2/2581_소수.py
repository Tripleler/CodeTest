# https://www.acmicpc.net/problem/2581

def prime(n):
    import math
    if n < 2:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, math.ceil(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True


m = int(input())
n = int(input())
answer = []
for i in range(m, n + 1):
    if prime(i):
        answer.append(i)
if answer:
    print(sum(answer))
    print(answer[0])
else:
    print(-1)

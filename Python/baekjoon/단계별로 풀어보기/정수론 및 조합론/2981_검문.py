# https://www.acmicpc.net/problem/2981

from sys import stdin

input = stdin.readline
l = []
for _ in range(int(input())):
    l.append(int(input()))
l.sort()
divisor = []
k = l[1] - l[0]
for i in range(2, int(k ** 0.5) + 1):  # divisor : 최댓값과 최솟값의 차이의 약수
    if k % i == 0:
        divisor.append(i)
        if k // i != i:
            divisor.append(int(k // i))
divisor.append(k)
answer = []
for i in divisor:  # 약수만 체크
    c = l[0] % i
    cond = True
    for j in l:
        if j % i != c:
            cond = False
            break
    if cond:
        answer.append(i)
answer.sort()
print(*answer)

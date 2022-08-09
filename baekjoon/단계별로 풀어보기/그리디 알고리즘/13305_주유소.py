# https://www.acmicpc.net/problem/13305

n = int(input())
d = list(map(int, input().split()))
p = list(map(int, input().split()))
a = p[0]
answer = 0
for x, y in zip(d, p[:-1]):
    if y < a:
        a = y
    answer += x * a
print(answer)

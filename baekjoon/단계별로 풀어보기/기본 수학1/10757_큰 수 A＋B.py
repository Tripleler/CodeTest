# https://www.acmicpc.net/problem/10757

# print(sum(map(int, input().split())))

a, b = input().split()
if len(a) != len(b):
    l = max(len(a), len(b))
    if l - len(a):
        a = '0' * (l - len(a)) + a
    else:
        b = '0' * (l - len(b)) + b
answer = ''
m = 0
for x, y in zip(a[::-1], b[::-1]):
    n = int(x) + int(y) + m
    answer += str(n)[-1]
    m = 1 if n >= 10 else 0
if m:
    answer += '1'
print(answer[::-1])

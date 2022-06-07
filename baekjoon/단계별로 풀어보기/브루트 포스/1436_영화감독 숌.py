# https://www.acmicpc.net/problem/1436

n = int(input())
cnt = 0
i = 5
while cnt < n:
    i += 1
    if '666' in str(i):
        cnt += 1
print(i)

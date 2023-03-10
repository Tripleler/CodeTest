# https://www.acmicpc.net/problem/1065

n = int(input())
if n < 100:
    print(n)
else:
    cnt = 99
    for i in range(100, n + 1):
        l = list(map(int, list(str(i))))
        if l[2] - l[1] == l[1] - l[0]:
            cnt += 1
    print(cnt)

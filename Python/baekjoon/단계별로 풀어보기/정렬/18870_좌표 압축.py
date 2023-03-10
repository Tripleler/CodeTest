# https://www.acmicpc.net/problem/18870

input()
li = list(map(int, input().split()))
s = sorted(list(set(li)))
dic = {k: v for v, k in enumerate(s)}
for x in li:
    print(dic[x], end=' ')

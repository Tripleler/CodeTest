# https://www.acmicpc.net/problem/2750

li = []
for _ in range(int(input())):
    li.append(int(input()))
for x in sorted(li):
    print(x)

# https://www.acmicpc.net/problem/1037

input()
l = sorted(list(map(int, input().split())))
print(l[0] * l[-1])

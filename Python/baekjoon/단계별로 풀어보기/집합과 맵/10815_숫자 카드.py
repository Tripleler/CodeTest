# https://www.acmicpc.net/problem/10815

input()
s = set(input().split())
input()
answer = ''
for x in input().split():
    answer += '1 ' if x in s else '0 '
print(answer)

# https://www.acmicpc.net/problem/1541

s = input().split('-')
answer = sum(map(int, s[0].split('+')))
for x in s[1:]:
    answer -= sum(map(int, x.split('+')))
print(answer)

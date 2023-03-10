# https://www.acmicpc.net/problem/10871

_, x = map(int, input().split())
s = ''
for i in map(int, input().split()):
    if i < x:
        s += f' {i}'
print(s.lstrip())

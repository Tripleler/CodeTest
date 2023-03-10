# https://www.acmicpc.net/problem/5622
# ABCDEFGHIJKLMNOPQRSTUVWXYZ

answer = 0
for s in input():
    if (s == 'Y') or (s == 'Z'):
        answer += 10
    elif s == 'V':
        answer += 9
    elif s == 'S':
        answer += 8
    else:
        answer += (ord(s) - 65)//3 + 3
print(answer)

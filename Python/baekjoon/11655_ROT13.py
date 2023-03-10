# https://www.acmicpc.net/problem/11655

import re

p = re.compile('[A-Za-z]')
s = input()
answer = ''
for x in s:
    if p.match(x):
        a = ord(x)
        if a >= ord('z') - 12:
            answer += chr(a - 13)
        elif a >= ord('a'):
            answer += chr(a + 13)
        elif a >= ord('Z') - 12:
            answer += chr(a - 13)
        else:
            answer += chr(a + 13)
    else:
        answer += x
print(answer)

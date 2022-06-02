# https://www.acmicpc.net/problem/1157

from collections import Counter

s = input().upper()
if len(s) == 1:
    print(s)
else:
    c = Counter(s).most_common(2)
    print('?') if c[0][1] == c[1][1] else print(c[0][0])

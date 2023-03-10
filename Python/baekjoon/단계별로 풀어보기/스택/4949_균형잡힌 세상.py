# https://www.acmicpc.net/problem/4949

import re
from sys import stdin

input = stdin.readline
while True:
    s = input().rstrip()
    if s == '.':
        break
    s = re.sub(r"[^\[\]\(\)]", "", s)
    while ('()' in s) or ('[]' in s):
        s = s.replace('()', '')
        s = s.replace('[]', '')
    print('no' if s else 'yes')

# https://www.acmicpc.net/problem/10816

from collections import Counter

input()
dic = Counter(input().split())
input()
print(' '.join([str(dic[x]) for x in input().split()]))

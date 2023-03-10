# https://www.acmicpc.net/problem/2798

from itertools import combinations

_, m = map(int, input().split())
cards = map(int, input().split())
print(max(x for x in map(sum, combinations(cards, 3)) if x <= m))

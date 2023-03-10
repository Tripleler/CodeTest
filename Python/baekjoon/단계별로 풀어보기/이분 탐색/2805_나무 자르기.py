# https://www.acmicpc.net/problem/2805

# n, m = map(int, input().split())
# trees = list(map(int, input().split()))
# trees.sort(reverse=True)
# left = 0
# right = max(trees)
# while left <= right:
#     mid = (left + right) // 2
#     total = 0
#     for tree in trees:
#         if tree <= mid:
#             break
#         total += (tree - mid)
#     if total >= m:
#         left = mid + 1
#     else:
#         right = mid - 1
# print(right)

from collections import Counter

n, m = map(int, input().split())
trees = sorted(Counter(map(int, input().split())).items(), reverse=True)
left = 0
right = trees[0][0]
while left <= right:
    mid = (left + right) // 2
    total = 0
    for tree, c in trees:
        if tree <= mid:
            break
        total += (tree - mid) * c
    if total >= m:
        left = mid + 1
    else:
        right = mid - 1
print(right)

# https://www.acmicpc.net/problem/1920

# def binary_search(n, array, start, end):
#     if start <= end:
#         mid = (start + end) // 2
#         if array[mid] == n:
#             return 1
#         elif array[mid] > n:
#             return binary_search(n, array, start, mid - 1)
#         else:
#             return binary_search(n, array, mid + 1, end)
#     else:
#         return 0
#
#
# end = int(input()) - 1
# A = sorted(list(map(int, input().split())))
# input()
# for x in map(int, input().split()):
#     print(binary_search(x, A, 0, end))

input()
A = set(input().split())
input()
for x in input().split():
    print(1 if x in A else 0)
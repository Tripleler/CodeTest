# https://www.acmicpc.net/problem/2110

from sys import stdin

input = stdin.readline
n, c = map(int, input().split())
coordinates = [int(input()) for _ in range(n)]
coordinates.sort()
distances = []
for i in range(n - 1):
    distances.append(coordinates[i + 1] - coordinates[i])
minimum = 1  # 최소거리
maximum = coordinates[-1] - coordinates[0]  # 최대 거리
while maximum >= minimum:
    mid = (maximum + minimum) // 2  # 단위 거리
    temp = 0
    cnt = 1
    for distance in distances:
        if temp + distance >= mid:
            cnt += 1
            temp = 0
        else:
            temp += distance
    if cnt >= c:  # 개수가 더 많으면 거리를 키움
        minimum = mid + 1
    else:
        maximum = mid - 1
print(maximum)

# from sys import stdin
#
# input = stdin.readline
# n, c = map(int, input().split())
# coordinates = [int(input()) for _ in range(n)]
# coordinates.sort()
# minimum = 1  # 최소거리
# maximum = coordinates[-1] - coordinates[0]  # 최대 거리
# while maximum >= minimum:
#     mid = (maximum + minimum) // 2  # 단위 거리
#     temp = coordinates[0]
#     cnt = 1
#     for i in range(1,n):
#         if coordinates[i] - temp >= mid:
#             cnt += 1
#             temp = coordinates[i]
#     if cnt >= c:  # 개수가 더 많으면 거리를 키움
#         minimum = mid + 1
#     else:
#         maximum = mid - 1
# print(maximum)
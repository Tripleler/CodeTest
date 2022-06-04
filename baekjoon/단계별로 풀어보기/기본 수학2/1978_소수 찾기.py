# https://www.acmicpc.net/problem/1978

import math

input()
nums = list(map(int, input().split()))
answer = 0
for num in nums:
    if num == 1:
        continue
    for i in range(2, math.ceil(math.sqrt(num)) + 1):
        if num % i == 0:
            break
    if (num % i != 0) or (num == 2):
        answer += 1
print(answer)


# def prime(n):
#     import math
#     if n < 2:
#         return False
#     elif n == 2:
#         return True
#     else:
#         for i in range(2, math.ceil(math.sqrt(n)) + 1):
#             if n % i == 0:
#                 return False
#         return True
#
#
# input()
# nums = list(map(int, input().split()))
# answer = 0
# for num in nums:
#     answer += prime(num)
# print(answer)

# https://www.acmicpc.net/problem/2775
# 파스칼의 삼각형

for _ in range(int(input())):
    k = int(input())
    n = int(input())
    answer = 1
    for i, x in enumerate(range(k + 2, n + k + 1), start=1):
        answer *= x
        answer /= i
    print(int(answer))

# import math
#
# for _ in range(int(input())):
#     k = int(input())
#     n = int(input())
#     print(math.comb(n + k, k + 1))

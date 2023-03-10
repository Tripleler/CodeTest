# https://www.acmicpc.net/problem/1929

# def prime(n):
#     if n < 2:
#         return False
#     elif n == 2:
#         return True
#     else:
#         if not n % 2:
#             return False
#         else:
#             for i in range(3, round(n ** 0.5) + 1, 2):
#                 if n % i == 0:
#                     return False
#             return True
#
#
# m, n = map(int, input().split())
# if m <= 2:
#     print(2)
# if not m % 2:
#     m += 1
# for i in range(m, n + 1, 2):
#     if prime(i):
#         print(i)

m, n = map(int, input().split())
prime = [False, False] + [True] * n
for i, cond in enumerate(prime):
    if cond:
        prime[2 * i::i] = [False] * len(prime[2 * i::i])
for j in range(m, n + 1):
    if prime[j]:
        print(j)

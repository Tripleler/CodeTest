# https://www.acmicpc.net/problem/2609

# a, b = sorted(map(int, input().split()))
# for i in range(a, 0, -1):
#     if (a % i == 0) and (b % i == 0):
#         break
# print(i)
# print(int(a * b / i))

a, b = sorted(map(int, input().split()))
x, y = a, b
while y:
    x, y = y, x % y
print(x)
print(int(a * b / x))

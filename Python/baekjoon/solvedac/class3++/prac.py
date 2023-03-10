# https://www.acmicpc.net/problem/1107


n = input()
l = len(n)
m = int(input())
cnt = abs(int(n) - 100)
buttons = set(str(x) for x in range(10)) - set(input().split())
for i in range(1000001):
    num = str(i)
    correct = True
    for j in num:
        if j in buttons:
            correct = False
            break
    if correct:
        cnt = min(cnt, abs(int(n)-int(num)) + l)
print(cnt)

# n = input()
# l = len(n)
# m = int(input())
# if not m:
#     print(min(abs(int(n) - 100), len(n)))
# else:
#     buttons = set(str(x) for x in range(10)) - set(input().split())
#     if m == 10:
#         print(abs(int(n) - 100))
#     else:
#         temp = []
#         for i in range(l):
#             k = int(n[:i + 2] + '0' * (l - i - 2))
#             choices = []
#             min_i = 10 ** l
#             for button in buttons:
#                 if not temp:
#                     if abs(int(button + '0' * (l - i - 1)) - k) < min_i:
#                         choices = [button]
#                         min_i = abs(int(button + '0' * (l - i - 1)) - k)
#                     elif abs(int(button + '0' * (l - i - 1)) - k) == min_i:
#                         choices.append(button)
#                 else:
#                     for t in temp:
#                         if abs(int(t + button + '0' * (l - i - 1)) - k) < min_i:
#                             choices = [t + button]
#                             min_i = abs(int(t + button + '0' * (l - i - 1)) - k)
#                         elif abs(int(t + button + '0' * (l - i - 1)) - k) == min_i:
#                             choices.append(t + button)
#             temp = choices
#         print(temp)
#         print(min(abs(int(n) - 100), abs(int(temp[0]) - int(n)) + l)) if temp else print(abs(int(n) - 100))

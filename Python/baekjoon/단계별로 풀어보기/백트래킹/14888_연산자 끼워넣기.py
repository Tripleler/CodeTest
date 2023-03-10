# https://www.acmicpc.net/problem/14888

from itertools import permutations

input()
nums = list(map(int, input().split()))
cals = []
for t, i in zip(['+', '-', '*', '/'], input().split()):
    cals += [t] * int(i)
answer = []
for t in set(permutations(cals)):
    cal = nums[0]
    for n, x in zip(nums[1:], t):
        if x == '+':
            cal += n
        elif x == '-':
            cal -= n
        elif x == '*':
            cal *= n
        elif x == '/':
            if cal >= 0:
                cal //= n
            else:
                cal = -(-cal // n)
    answer.append(cal)
print(max(answer))
print(min(answer))

# https://www.acmicpc.net/problem/17298

input()
stack = list(map(int, input().split()))
n = stack.pop(-1)
check = [n]
answer = [-1]
for x in reversed(stack):
    while True:
        if check:
            n = check.pop(-1)
        else:
            answer.append(-1)
            n = x
            check.append(n)
            break
        if x < n:
            check.append(n)
            check.append(x)
            answer.append(n)
            break
print(*reversed(answer))

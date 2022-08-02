# https://www.acmicpc.net/problem/24416

n = int(input())
fibo = [1, 1, 2, 3]
while len(fibo) != n:
    fibo.append(fibo[-1] + fibo[-2])
print(fibo[-1], n - 2)

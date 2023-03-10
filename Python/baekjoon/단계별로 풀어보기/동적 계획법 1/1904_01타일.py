# https://www.acmicpc.net/problem/1904

n = int(input())
fibo = [1, 1]
while len(fibo) <= n:
    fibo.append((fibo[-1] + fibo[-2]) % 15746)
print(fibo[-1] % 15746)

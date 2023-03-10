# https://www.acmicpc.net/problem/4673

l = [False] + [True] * 10000
i = 1
while i < 10000:
    if l[i]:
        print(i)
        j = i + sum(map(int, list(str(i))))
        while j < 10000:
            l[j] = False
            j = j + sum(map(int, list(str(j))))
    i += 1

# https://www.acmicpc.net/problem/10809

li = [-1] * 26
for i, s in enumerate(input()):
    if li[ord(s) - 97] == -1:
        li[ord(s) - 97] = i
print(' '.join(map(str, li)))

# https://www.acmicpc.net/problem/14681

x = False if input().startswith('-') else True
y = False if input().startswith('-') else True
if x and y:
    print(1)
elif not x and y:
    print(2)
elif not x and not y:
    print(3)
else:
    print(4)

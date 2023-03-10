# https://www.acmicpc.net/problem/2941

p = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
s = input()
for x in p:
    s = s.replace(x, 'a')
print(len(s))

import re

p = re.compile('[A-Z]')

st = input()
print(''.join(p.findall(st)))

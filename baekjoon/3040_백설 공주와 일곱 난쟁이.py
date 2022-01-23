from sys import stdin
import itertools

member = []
for _ in range(9):
    member.append(int(*stdin.readline().split()))
total = sum(member)
for i in itertools.combinations(member, 2):
    if total - sum(i) == 100:
        break
member.remove(i[0])
member.remove(i[1])
for num in member:
    print(num)

import sys

passenger = 0
passenger_list = []
for _ in range(9):
    inner, outer = map(int, sys.stdin.readline().split())
    passenger += (outer - inner)
    passenger_list.append(passenger)
print(max(passenger_list))

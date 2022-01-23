left = [1, 4, 7]
right = [3, 6, 9]


def dist(x, y):
    loc = {1: [0, 0], 2: [0, 1], 3: [0, 2], 4: [1, 0], 5: [1, 1], 6: [1, 2], 7: [2, 0], 8: [2, 1], 9: [2, 2], 0: [3, 1],
           11: [3, 0], 12: [3, 2]}
    return abs(loc[x][0] - loc[y][0]) + abs(loc[x][1] - loc[y][1])


def solution(numbers, hand):
    result = ''
    right_loc = 12
    left_loc = 11
    for i in numbers:
        if i in left:
            result += 'L'
            left_loc = i
        elif i in right:
            result += 'R'
            right_loc = i
        else:
            if hand == 'left':
                if dist(left_loc, i) <= dist(right_loc, i):
                    result += 'L'
                    left_loc = i
                else:
                    result += 'R'
                    right_loc = i
            else:
                if dist(left_loc, i) >= dist(right_loc, i):
                    result += 'R'
                    right_loc = i
                else:
                    result += 'L'
                    left_loc = i
    return result


print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right"))

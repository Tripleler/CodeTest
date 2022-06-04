from sys import stdin


def readlines(count):
    result = []
    for _ in range(count):
        result.append(*stdin.readline().split())
    return result


# ABCDEFGHIJKLMNOPQRSTUVWXYZ

from sys import stdin

input = stdin.readline


def prime(n):
    if n < 2:
        return False
    elif not n % 2:
        return True if n == 2 else False
    else:
        for i in range(3, round(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

from sys import stdin


def readlines(count):
    result = []
    for _ in range(count):
        result.append(*stdin.readline().split())
    return result

from sys import stdin

input = stdin.readline
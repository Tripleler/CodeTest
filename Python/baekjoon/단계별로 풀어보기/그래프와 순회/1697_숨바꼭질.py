# https://www.acmicpc.net/problem/1697

def bfs():
    global n, k
    visit = [True] * 100001
    q = set([n])
    cnt = 1
    while True:
        temp = []
        for x in q:
            if (x - 1 == k) or (x + 1 == k) or (x * 2 == k):
                return cnt
            if (0 <= x - 1 <= 100000) and visit[x - 1]:
                temp.append(x - 1)
                visit[x - 1] = False
            if (0 <= x + 1 <= 100000) and visit[x + 1]:
                temp.append(x + 1)
                visit[x + 1] = False
            if (0 <= x * 2 <= 100000) and visit[x * 2]:
                temp.append(x * 2)
                visit[x * 2] = False
        q = temp
        cnt += 1


n, k = map(int, input().split())
if n == k:
    print(0)
else:
    print(bfs())


# def find(n, k):
#     if n >= k:  # n >= k 이면 두배해봤자 소용x 이므로 차이를 리턴
#         return n - k
#     elif k == 1:  # k == 1이면 n == 0이므로 1을 리턴
#         return 1
#     elif k % 2:  # 홀수이면 짝수로 맞춰주기, 맞추는 +-이동으로 + 1
#         return min(find(n, k - 1), find(n, k + 1)) + 1
#     else:  # 짝수이면 반례는 6, 16 -> 6, 8 여기서 6, 4보다는 8-6이 빠름
#         return min(k - n, find(n, k // 2) + 1)
#
#
# n, k = map(int, input().split())
# print(find(n, k))

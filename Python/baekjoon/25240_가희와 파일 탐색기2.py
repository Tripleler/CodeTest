# https://www.acmicpc.net/problem/25240

from sys import stdin

input = stdin.readline


def check(admin, cond):
    admin = bin(int(admin))[2:]
    if len(admin) == 1:
        admin = '00' + admin[-1]
    elif len(admin) == 2:
        admin = '0' + admin[-2:]
    if cond == 'R':
        print(1 if admin[0] == '1' else 0)
    if cond == 'W':
        print(1 if admin[1] == '1' else 0)
    if cond == 'X':
        print(1 if admin[2] == '1' else 0)


u, f = map(int, input().split())
group = {}

for _ in range(u):
    s = input().split()
    if len(s) == 2:  # 그룹에 속해있다면 {이름:그룹명리스트}
        group[s[0]] = s[1].split(',')

dic = {}

for _ in range(f):  # {파일명 : {admin:admin, u_name:u_name, g_name:g_name}}
    f_name, admin, u_name, g_name = input().split()
    f_dic = {
        'admin': admin,
        'user_name': u_name,
        'group_name': g_name
    }
    dic[f_name] = f_dic

for _ in range(int(input())):
    u_name, f_name, cond = input().split()
    f_name = dic[f_name]
    if u_name == f_name['user_name']:  # 파일명의 u_name 과 요청자명이 같으면
        admin = f_name['admin'][0]
    elif (u_name == f_name['group_name']) or (u_name in group.keys() and f_name['group_name'] in group[u_name]):
        # 파일명의 g_name 과 요청자명이 같거나 혹은 (요청자명이 파일명의 g_name 에 속하면)
        admin = f_name['admin'][1]
    else:  # other
        admin = f_name['admin'][2]
    check(admin, cond)
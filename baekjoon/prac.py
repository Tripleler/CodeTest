def check(ad, co):
    if len(ad) == 3:
        ad = '0b00' + ad[-1]
    elif len(ad) == 4:
        ad = '0b0' + ad[-2:]
    if co == 'R':
        print(1 if int(ad[2]) else 0)
    if co == 'W':
        print(1 if int(ad[3]) else 0)
    if co == 'X':
        print(1 if int(ad[4]) else 0)


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
        admin = bin(int(f_name['admin'][0]))
        check(admin, cond)
    elif (u_name == f_name['group_name']) or (u_name in group.keys() and f_name['group_name'] in group[u_name]):
        # 파일명의 g_name 과 요청자명이 같거나 혹은 (요청자명이 파일명의 g_name 에 속하면)
        admin = bin(int(f_name['admin'][1]))
        check(admin, cond)
    else:  # other
        admin = bin(int(f_name['admin'][2]))
        check(admin, cond)

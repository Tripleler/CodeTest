# https://www.acmicpc.net/problem/11478

s = input()
l = len(s)
cnt = 0
i = 1
for k in range(l):
    st = set()
    for j in range(l + 1 - i):
        st.add(s[j:j + i])
    i += 1
    cnt += len(st)
print(cnt)

# https://www.acmicpc.net/problem/9935

# st = input()
# ex = input()
# while True:
#     n = len(st)
#     st = st.replace(ex, "")
#     if len(st) == n:
#         break
# print(st if st else "FRULA")

st = input()
ex = input()
stack = []
end = ex[-1]
n = len(ex)
for s in st:
    stack.append(s)
    if s == end:  # 끝 문자열이 같으면
        if "".join(stack[-n:]) == ex:  # 단위문자열이면
            for _ in range(n):
                stack.pop(-1)  # 제거
print("".join(stack)) if stack else print("FRULA")

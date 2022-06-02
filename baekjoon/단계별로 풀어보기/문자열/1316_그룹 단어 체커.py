# https://www.acmicpc.net/problem/1316

answer = 0
for _ in range(int(input())):
    s = input()
    st = set()
    d = ''
    for x in s:
        if x != d:
            d = x
            if d in st:
                answer -= 1
                break
            st.add(d)
    answer += 1
print(answer)

# result = 0
# for i in range(int(input())):
#     word = input()
#     if list(word) == sorted(word, key=word.find):
#         result += 1
# print(result)

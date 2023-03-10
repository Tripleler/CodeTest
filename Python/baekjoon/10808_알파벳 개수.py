from collections import Counter

dic = Counter(list(input()))
print(' '.join([str(dic[chr(i)]) for i in range(97, 123)]))

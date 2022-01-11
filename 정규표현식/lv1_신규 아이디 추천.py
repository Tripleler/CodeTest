import re
def solution(new_id):
    new_id = new_id.lower() # 1
    new_id = re.sub('[^0-9a-z\-\_\.]+', '', new_id) #2
    new_id = re.sub('\.+', '.', new_id) #3
    new_id = re.sub('^\.|\.$', '', new_id) #4
    if new_id == '': #5
        new_id = 'a'
    new_id = new_id[:15] #6
    if new_id[-1] == '.':
        new_id = new_id[:-1]
    while len(new_id) <= 2: #7
        new_id += new_id[-1]
    return new_id

print(solution("...!@BaT#*..y.abcdefghijklm"))
print(solution("z-+.^."))
print(solution("=.="))
print(solution("123_.def"))
print(solution("abcdefghijklmn.p"))
def solution(s):
    try:
        a=int(s)
    except:
        return False
    else:
        if (len(s)==4)|(len(s)==6):
            return True
        else:
            return False
print(solution("a234"), solution("1234"))

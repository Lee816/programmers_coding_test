def solution(s, n):
    answer = ""
    
    for x in s:
        if (ord(x)+n) > ord("z") and x.islower():
            answer += chr(ord("a")+((ord(x)+n)-ord("z"))-1)
        elif (ord(x)+n) > ord("Z") and x.isupper():
            answer += chr(ord("A")+((ord(x)+n)-ord("Z"))-1)
        elif x == " ":
            answer += " "
        else:
            answer += chr(ord(x)+n)
    
    return answer
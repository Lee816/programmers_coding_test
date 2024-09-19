def solution(s):
    answer = []
    
    for x in s:
        if answer and answer[-1] == x:
            answer.pop()
        else:
            answer.append(x)
            
    return 0 if answer else 1
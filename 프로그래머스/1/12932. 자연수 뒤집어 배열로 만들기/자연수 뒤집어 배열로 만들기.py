def solution(n):
    answer = list(int(x) for x in list(str(n)))
    answer.reverse()
    
    return answer
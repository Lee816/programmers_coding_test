def solution(n):
    
    answer = [x for x in list(str(n))]
    answer.sort()
    answer.reverse()

    return int("".join(x for x in answer))
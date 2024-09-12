def solution(numLog):
    answer = ""
    for i in range(1,len(numLog)):
        if  numLog[i]-numLog[i-1] in [1,-1]:
            if numLog[i] > numLog[i-1]:
                answer += "w"
            else:
                answer += "s"

        if numLog[i]-numLog[i-1] in [10,-10]:
            if numLog[i] > numLog[i-1]:
                answer += "d"
            else:
                answer += "a"
                
    return answer
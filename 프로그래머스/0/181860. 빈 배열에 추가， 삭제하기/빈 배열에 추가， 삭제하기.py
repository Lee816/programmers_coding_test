def solution(arr, flag):
    answer = []
    for idx, val in enumerate(flag):
        if val == True:
            answer += [arr[idx]]*arr[idx]*2
        else:
            answer = answer[:len(answer)-arr[idx]]
    return answer
def solution(A, B):
    if A==B:
        return 0
    else:
        for x in range(1,len(A)+1):
            if A[-1]+A[0:-1] == B:
                return x
            else:
                A = A[-1]+A[0:-1]
            
    return -1
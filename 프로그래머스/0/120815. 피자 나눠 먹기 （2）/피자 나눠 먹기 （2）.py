def solution(n):
    for x in range(1,n+1):
        if (x*6)%n == 0:
            return x
def solution(n):
    answer = []
    for x in range(1,n+1):
        if (x%2==0 and x//2!=1) or (x%3==0 and x//3!=1) or (x%5==0 and x//5!=1) or (x%7==0 and x//7!=1):
            answer.append(x)
    return len(answer)
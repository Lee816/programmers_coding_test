def solution(a, b, c):
    if len(set([a,b,c])) == 1:
        return (a+b+c)*(a**2+b**2+c**2)*(a**3+b**3+c**3)
    elif len(set([a,b,c])) == 2:
        return (a+b+c)*(a**2+b**2+c**2)
    else :
        return a+b+c
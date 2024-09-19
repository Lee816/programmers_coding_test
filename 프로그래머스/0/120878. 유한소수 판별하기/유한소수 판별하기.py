def solution(a, b):
    aset = set([x for x in range(1,a+1) if a%x==0])
    bset = set([x for x in range(1,b+1) if b%x==0])
    maxset = max(list(aset & bset))
    return 2 if [x for x in range(2,(b//maxset)+1) if (b//maxset)%x==0 and x%2!=0 and x%5!=0] else 1
        
        
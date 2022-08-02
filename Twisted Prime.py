for n in range (1,201):
    temp=n
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c+=1
    if c==2:
        N=0
        while n>0:
            r=n%10
            N=N*10+r
            n//=10
        C=0
        for i in range(1,N+1):
            if N%i==0:
                C+=1
        if C==2:
            print(temp,' is a Twisted Prime.')

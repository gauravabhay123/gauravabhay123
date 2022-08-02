for n in range(10000,30001):
    c=0
    s=0
    for i in range(1,n+1):
        if n%i==0:
            c+=1
            s+=i
    S=0
    for i in range(1,c):
        if c%i==0:
            S+=i
    if S==c:
        w=0
        for i in range(1,s):
            if s%i==0:
                w+=i
        if w==s:
            print(n,'is a Sublime No.')
                

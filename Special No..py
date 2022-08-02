for n in range (1,10000001):
    s=0
    temp=n
    while n>0:
        r=n%10
        f=1
        for i in range(1,r+1):
            f*=i
        n//=10
        s+=f
    if s==temp:
        print(temp,'is a Special No.')
    #else:
        #print('Not a Special No.')


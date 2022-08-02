for n in range(1,100001):
    temp=n
    s=0
    N=0
    while n>0:
        r=n%10
        N=N*10+r
        n//=10
    c=1
    while N>0:
        R=N%10
        s+=R**c
        N//=10
        c+=1
    if s==temp:
        print(temp,' is a Disarium No.')

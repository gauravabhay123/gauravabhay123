for n in range(1,1001):
    s=0
    temp=n
    while n>0:
        r=n%10
        s+=r
        n//=10
    if temp%s==0:
        print(temp,'is a Harshad No.')

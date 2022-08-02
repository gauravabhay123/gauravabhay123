for n in range (1,100001):    #n=int(input('Enter the number : '))
    s=0
    for i in range (1,n):
        if n%i==0:
            s+=i
    if s==n:
        print(n,'is a Perfect No.')
    #else:
        #print('Not a Perfect No.')

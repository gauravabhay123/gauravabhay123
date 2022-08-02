for n in range (1,501):    #n=int(input('Enter the number : '))
    s=0
    for i in range (1,n):
        if n%i==0:
            s+=i
    if s<n:
        print(n,'is a Deficient No.')
        

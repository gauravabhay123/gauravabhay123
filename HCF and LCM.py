n1=int(input('Enter Number 1: '))
n2=int(input('Enter Number 2: '))

hcf=1
lcm=0
f=1
if n1>n2:
    for i in range (1,n1+1):
        if n1%i==0 and n2%i==0:
            hcf=i
    while lcm==0:
        m=n2*f
        for i in range (1,f+1):
            l=n1*i
            if m==l:
                lcm=l
        f+=1
else:
    for i in range(1,n2+2):
        if n1%i==0 and n2%i==0:
            hcf=i
    while lcm==0:
        m=n1*f
        for i in range (1,f+1):
            l=n2*i
            if m==l:
                lcm=l
        f+=1
print('HCF is',hcf)
print('LCM is',lcm)
        

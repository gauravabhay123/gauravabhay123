n=int(input('Enter number of terms(more than 2) : '))
n1=0
n2=1
print('Fibonacci series : ',n1,end=', ')
print(n2,end=', ')
for i in range(n-2):
    n=n1+n2
    print(n,end=', ')
    n1=n2
    n2=n

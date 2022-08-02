'''
An abundant Number (also known as excessive number)
is a number in the number theory which itself is smaller
than the sum of all its proper divisors.
For example,12 is an abundant Number : divisors 1,2,3,4,6 , sum =16 >12.
eg. 12, 18
'''

n=int(input('Enter the number : '))
s=0
for i in range (1,n):
    if n%i==0:
        s+=i
if s>n:
    print(n,'is an Abundant No.')
else:
    print(n,'is not an Abundant No.')
    

        

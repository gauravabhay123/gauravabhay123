
def repeat_roman():

    Num=[1,5,10,50,100,500,1000]
    Rom=['I','V','X','L','C','D','M']

    n=int(input("Enter the Number:"))
    num=n
    pv=1
    roman=''
    
    while n>0:
        u=(n%10)*pv
        n=n//10
    
        if u!=0:
            if u in Num:
                R=Rom[Num.index(u)]
                roman=R+roman
            else:
                if u < 5*pv:
                    a=int(u/(1*pv))
                    if u <= 3*pv:
                        R=Rom[Num.index(1*pv)]*a
                        roman=R+roman
                    else:
                        R=Rom[Num.index(1*pv)]+Rom[Num.index(5*pv)]
                        roman=R+roman

                else:
                    a=int(u/(1*pv))
                    if u <= (8*pv):
                        R=Rom[Num.index(5*pv)]+(Rom[Num.index(1*pv)]*(a-5))
                        roman=R+roman
                    else:
                        R=Rom[Num.index(1*pv)]+Rom[Num.index(10*pv)]
                        roman=R+roman
    
        pv*=10

    print('Roman Equivalent of',num,'is:',roman)

ans='1'
while True:           
    if ans=='1':
        repeat_roman()
    elif ans=='0':
        break
    else:
        print('Invalid Input! ABORTING!!')
        break
    ans=input("Press '1' to continue and '0' to quit : ")

    

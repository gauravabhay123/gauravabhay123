#----------------------------------------------------
# INSERTION SORTING
#----------------------------------------------------


L=[2,85,94,12,45,86,35,100]
print("Original List",L)

n=len(L)

for i in range (1,n):
    key=L[i]
    j=i-1

    while j>=0 and key<L[j]:
        L[j+1]=L[j]
        j=j-1

    else:
        L[j+1]=key
    #print("Refreshed list : ",L)
print('Sorted List',L)

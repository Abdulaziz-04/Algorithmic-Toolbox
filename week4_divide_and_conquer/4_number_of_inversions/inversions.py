# Uses python3
import sys

def merge(a,b,l,m,r):
    ic=0
    i=l
    j=m+1
    k=l

    while(i<=m and j<=r):
        if(a[i]<=a[j]):
            b[k]=a[i]
            i+=1
            k+=1
        else:
            b[k]=a[j]   # for case  [1,3,5] [2,4,6]   here 3 >2 and so will be 5 so inv_count must be mid-i
            ic+=m-i+1
            k+=1
            j+=1

    while(i<=m):
        b[k]=a[i]
        i+=1
        k+=1

    while(j<=r):
        b[k]=a[j]
        j+=1
        k+=1
    for i in range(l,r+1):
        a[i]=b[i]


    return ic



def get_number_of_inversions(a, b, l, r):
    ic=0
    if(l<r):
        m=(l+r)//2
        ic+=get_number_of_inversions(a,b,l,m)
        ic+=get_number_of_inversions(a,b,m+1,r)
        ic+=merge(a,b,l,m,r)
    return ic 

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b = n * [0]
    print(get_number_of_inversions(a, b, 0, len(a)-1))

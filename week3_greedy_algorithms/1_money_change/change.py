# Uses python3
import sys

def get_change(m):
    #write your code here
    c=0
    for i in [10,5,1]:
        if(m%i==0):
            return c+m//i
        else:
            d=m//i
            m-=d*i
            c+=d



    return m

if __name__ == '__main__':
    m=int(input())
    print(get_change(m))

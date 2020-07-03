# Uses python3
import sys
import math

def pisanoperiod(m):
    periods=[]
    a=0
    b=1
    periods.append(a%m)
    periods.append(b%m)
    while(True):
        c=a+b
        a=b
        b=c
        periods.append(c%m)
        for i in range(2,len(periods)-2):
            if(periods[i]==0 and periods[i+1]==1 and periods[i+2]==1):
                return len(periods)-3

def fib(n):
    a=0
    b=1
    if(n==0): return 0
    if(n==1): return 1
    for i in range(2,n+1):
        c=a+b
        a=b
        b=c
    return c


#reduce number by modulus of pisanoperiod
def get_fibonacci_huge_naive(n, m):
    val=n%pisanoperiod(m)
    fibnum=fib(val)
    return fibnum%m

    
if __name__ == '__main__':
    n, m = map(int, input().split())
    print(get_fibonacci_huge_naive(n, m))

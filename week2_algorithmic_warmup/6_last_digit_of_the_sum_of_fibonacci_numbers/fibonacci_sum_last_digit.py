# Uses python3
import sys
fibval=[1]*62

def fib(n):
    a=0
    b=1
    sm=a+b
    fibval[0]=0
    fibval[1]=1
    if(n==0): return 0
    if(n==1): return 1
    for i in range(2,n+1):
        c=(a+b)%10
        a=b
        b=c
        sm+=c
        fibval[i]=sm%10

def fibonacci_sum_naive(n):
    fib(60)
    return fibval[n%60]



if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum_naive(n))

# Uses python3
from sys import stdin
fibval=[1]*62

def fib(n):
    a=0
    b=1
    fibval[0]=0
    fibval[1]=1
    sm=a+b
    for i in range(2,n+1):
        c=(a+b)%10
        d=c**2
        a=b
        b=c
        sm+=d%10
        fibval[i]=sm%10
def fibonacci_sum_squares_naive(n):
    fib(60)
    return fibval[n%60]

if __name__ == '__main__':
    n=int(input())
    print(fibonacci_sum_squares_naive(n))

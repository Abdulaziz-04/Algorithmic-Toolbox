# Uses python3
import sys
fibval=[0]*62

def seqfib(m,n):
    finsum=0
    if(n<m): n+=60
    #sometimes the value of m and n may interchange such that n<m so adding 60 and then looping through mod 60 shoulld do the trick
    for i in range(m,n+1):
        finsum+=fibval[i%60]
    return finsum%10




def fib(n): 
    a=0
    b=1
    sm=0
    fibval[0]=0
    fibval[1]=1
    for i in range(2,n+1):
        c=(a+b)%10
        a,b=b,c
        fibval[i]=c


def fibonacci_partial_sum_naive(from_, to):
    fib(60)
    #pisano period for 10 is 60
    return seqfib(from_%60,to%60)




if __name__ == '__main__':
    from_, to = map(int, input().split())
    print(fibonacci_partial_sum_naive(from_, to))
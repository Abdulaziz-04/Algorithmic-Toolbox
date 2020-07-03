# Uses python3
import sys

def get_fibonacci_last_digit_naive(n):
    a=0
    b=1
    for i in range(2,n+1):
        c=(a+b)%10
        a=b
        b=c
    return c
        
if __name__ == '__main__':
    n = int(input())
    print(get_fibonacci_last_digit_naive(n))

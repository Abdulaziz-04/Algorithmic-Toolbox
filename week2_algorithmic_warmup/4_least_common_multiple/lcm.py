# Uses python3
import sys

def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)

def lcm_naive(a, b):
    val=gcd(a,b)
    return a*b//val
    

if __name__ == '__main__':
    a, b = map(int, input().split())
    print(lcm_naive(a, b))


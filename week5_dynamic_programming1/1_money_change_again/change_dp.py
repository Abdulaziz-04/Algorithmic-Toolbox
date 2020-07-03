# Uses python3
import sys

def get_change(m):
    #write your code here
    #1 3 and 4 are the given monetization values
    d=[1,3,4]
    coins=[0]*(m+1)
    #build array from scratch adding values from scratch 
    for j in range(1,m+1):
        val=10000
        for i in d:
            if(j>=i):
                val=min(val,1+coins[j-i])
        coins[j]=val
    return coins[m]




if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))

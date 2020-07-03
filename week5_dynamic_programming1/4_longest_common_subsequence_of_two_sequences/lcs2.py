#Uses python3

import sys

def lcs2(a, b,n,m):
    cs=[[0 for x in range(m+1)]for y in range(n+1)]
    for i in range(n+1):
        for j in range(m+1):
            if(i==0 or j==0):
                cs[i][j]=0
            elif(a[i-1]==b[j-1]):
                cs[i][j]=cs[i-1][j-1]+1
            else:
                cs[i][j]=max(cs[i-1][j],cs[i][j-1])
    return cs[n][m]
    #write your code here

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    print(lcs2(a, b,len(a),len(b)))

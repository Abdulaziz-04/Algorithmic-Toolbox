#Uses python3

import sys

def lcs3(a, b, c,p, q,r):
    cs=[[[0 for i in range(r+1)]for j in range(q+1)]for k in range(p+1)]
    for i in range(p+1):
        for j in range(q+1):
            for k in range(r+1):
                if(i==0 or j==0 or k==0):
                    cs[i][j][k]=0
                elif(a[i-1]==b[j-1]==c[k-1]):
                    cs[i][j][k]=cs[i-1][j-1][k-1]+1
                else:
                    cs[i][j][k]=max(cs[i-1][j][k],cs[i][j-1][k],cs[i][j][k-1])
    #write your code here
    return cs[p][q][r] 

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    an = data[0]
    data = data[1:]
    a = data[:an]
    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[:bn]
    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[:cn]
    print(lcs3(a, b, c,len(a),len(b),len(c)))

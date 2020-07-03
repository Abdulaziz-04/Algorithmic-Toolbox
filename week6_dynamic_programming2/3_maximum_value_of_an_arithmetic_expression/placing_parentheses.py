# Uses python3
def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

def MinMax(i,j,ops,mini,maxi):
    dmin=10000
    dmax=-10000
    for k in range(i,j):
        a=evalt(mini[i][k],maxi[k+1][j],ops[k])
        b=evalt(mini[i][k],mini[k+1][j],ops[k])
        c=evalt(maxi[i][k],maxi[k+1][j],ops[k])
        d=evalt(maxi[i][k],mini[k+1][j],ops[k])
        dmin=min(dmin,a,b,c,d)
        dmax=max(dmax,a,b,c,d)
    return dmin,dmax


def get_maximum_value(dataset):
    digits=[]
    for i in range(0,len(dataset)+1,2):
        digits.append(int(dataset[i]))
    ops=list(dataset[1:len(dataset):2])
    n=len(digits)
    mini=[[0 for i in range(n)]for j in range(n)]
    maxi=[[0 for i in range(n)]for j in range(n)]
    for i in range(n):
        mini[i][i]=digits[i]
        maxi[i][i]=digits[i]
    for s in range(1,n):
        for i in range(n-s):
            j=i+s
            mini[i][j],maxi[i][j]=MinMax(i,j,ops,mini,maxi)
    return maxi[0][n-1]


if __name__ == "__main__":
    print(get_maximum_value(input()))

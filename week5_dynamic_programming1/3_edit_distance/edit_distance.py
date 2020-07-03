# Uses python3
def edit_distance(s, t,n,m):
    strMat=[[0 for i in range(m+1) ]for j in range(n+1)]
    for i in range(n+1):
        for j in range(m+1):
            if(i==0):
                strMat[i][j]=j
            elif(j==0):
                strMat[i][j]=i
            elif(s[i-1]==t[j-1]):
                strMat[i][j]=strMat[i-1][j-1]
            else:
                strMat[i][j]=min(strMat[i-1][j],strMat[i][j-1],strMat[i-1][j-1])+1
    #write your code here
    return strMat[n][m]

if __name__ == "__main__":
    s1=input()
    s2=input()
    print(edit_distance(s1,s2,len(s1),len(s2)))
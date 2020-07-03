# Uses python3
import sys

def optimal_weight(W, w):
    # write your code here
    caps=[[0 for i in range(W+1)]for j in range(len(w)+1)]
    for i in range(len(w)+1):
        for j in range(W+1):
            #initially set all values to zero
            if(i==0 or j==0):
                caps[i][j]=0
            #going through all values of weights and determining the optimal values
            elif(w[i-1]<=j):
                caps[i][j]=max(w[i-1]+caps[i-1][j-w[i-1]],caps[i-1][j])
            #or else add the previous optimized value
            else:
                caps[i][j]=caps[i-1][j]
    return caps[len(w)][W]

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))

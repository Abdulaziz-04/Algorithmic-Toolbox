# Uses python3
import sys

def optimal_sequence(n):
    costs=[0]*(n+1)
    for i in range(2,n+1):
        min1=100000
        min2=100000
        if(i%2==0): min1=costs[i//2]
        if(i%3==0): min2=costs[i//3]
        costs[i]=min(costs[i-1],min1,min2)+1
    return sequence(n,costs)

def sequence(n,costs):
    numbers=[]
    while n>0:
        numbers.append(n)
        if(n%2!=0 and n%3!=0):
            n-=1
        elif(n%2==0 and n%3==0):
            n=n//3
        elif(n%2==0):
            if(costs[n-1]<costs[n//2]):
                n-=1
            else:
                n=n//2
        elif(n%3==0):
            if(costs[n-1]<costs[n//3]):
                n-=1
            else:
                n=n//3
    return reversed(numbers)



input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')

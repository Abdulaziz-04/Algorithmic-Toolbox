# Uses python3
import sys

def get_majority_element(a, left, right):
    #write your code here
    eleCount={}
    for i in a:
        if(i in eleCount):
            eleCount[i]+=1
        else:
            eleCount[i]=1
    for i in eleCount.values():
        if(i>len(a)//2):
            return 0
    return -1




    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)

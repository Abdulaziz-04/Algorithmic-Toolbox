#Uses python3

import sys
import itertools
from functools import cmp_to_key

def largest_number(a):
    res = sorted(a, key = cmp_to_key(lambda i, j: -1 if str(j) + str(i) < str(i) + str(j) else 1))
    res="".join(res)
    return res
'''def largest_number(a):
    #write your code here
    mx=0
    tmp=[]
    for i in a:
        if(len(i)>mx):
            mx=len(i)
    transition={}
    for i in a:
        num=''
        while(len(num)!=mx):
            num+=i
        tmp.append(num)
        transition[num]=i
    for i in tmp:
        i=int(i)
    tmp.sort(reverse=True)
    number=''
    for i in tmp:
        number+=transition[str(i)]
    return number'''

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
    

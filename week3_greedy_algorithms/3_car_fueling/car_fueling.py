# python3
import sys


def compute_min_refills(distance, tank, stops):
    stops.insert(0,0)
    stops.append(distance)
    refillCount=0
    w=len(stops)-1
    c=0
    while(c!=w):
        l=c
        while(c!=w and stops[c+1]-stops[l]<=tank):
            c+=1
        if(c==l):
            return -1
        if(c!=w):
            refillCount+=1
    return refillCount
        
    

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))

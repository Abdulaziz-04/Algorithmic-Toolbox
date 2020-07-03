# Uses python3
import sys

def selectMin(segments):
    segments.sort(key=lambda x:x[1])
    return segments[0][1]


def optimal_points(segments):
    rightend=[]
    points=[]
    j=0
    while(len(segments)!=0):
        i=selectMin(segments)
        while(len(segments)>0 and i>=segments[j][0] and i<=segments[j][1]): 
            points.append(i)
            segments.pop(j)
    return list(set(points))







    #write your code here
    

if __name__ == '__main__':
    segments=[]
    n=int(input())
    for i in range(n):
        a,b=map(int,input().split())
        segments.append([a,b])
    points=optimal_points(segments)
    print(len(points))
    print(*points)
    #input = sys.stdin.read()
    #n, *data = map(int, input().split())
    #segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    #points = optimal_points(segments)
    #print(len(points))
    #print(*points)

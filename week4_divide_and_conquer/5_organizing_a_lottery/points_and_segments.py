# Uses python3
import sys

def fast_count_segments(starts, ends, points):
    cnt={}
    lottery=[(x,'l') for x in starts]
    lottery+=[(x,'r') for x in ends]
    lottery+=[(x,'p') for x in points]
    lottery.sort()
    k=0
    c=0
    for i in lottery:
        if(i[1]=='l'):
            c+=1
        elif(i[1]=='r'):
            c-=1
        else:
            cnt[i[0]]=c
            k+=1
    return cnt 

def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    #use fast_count_segments
    cnt = fast_count_segments(starts, ends, points)
    for x in points:
        print(cnt[x], end=' ')

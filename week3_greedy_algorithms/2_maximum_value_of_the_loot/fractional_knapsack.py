# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value=0
    cw={}#Corresponding weights
    vpw=[] # value per unit weight
    for i in range(len(values)):
        vpw.append(values[i]/weights[i])
        cw[vpw[i]]=weights[i]
    vpw.sort(reverse=True)
    for i in range(len(vpw)):
        if(cw[vpw[i]]>capacity):
            value+=capacity*vpw[i]
            return value
        else:
            value+=vpw[i]*cw[vpw[i]]
            capacity-=cw[vpw[i]]
    return value


if __name__ == "__main__":
    data = list(map(int, input().split()))
    values=[]
    weights=[]
    capacity=data[1]
    for i in range(data[0]):
        v,w=map(int,input().split())
        values.append(v)
        weights.append(w)
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))

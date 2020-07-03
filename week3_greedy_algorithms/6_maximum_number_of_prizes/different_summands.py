# Uses python3
import sys

def optimal_summands(n):
    summands = []
    right = n
    left = 1
    '''In order to get distinct numbers we can go for sequence 1,2,3.. i.e. sum of 
    all natural numbers hence we arrive to a condition that S<=n and going technically we can conclude that
    after exceeding n/2 there won't be much optimization hence we start from 1 and reduce the values from n'''

    while right != 0:
        if left < right / 2:
            summands.append(left)
            right -= left
        else:
            summands.append(right)
            right = 0
        left += 1

    return summands
    


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')

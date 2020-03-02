# Uses python3
import sys

def get_majority_element(a, left, right):
    if left == right:
        return -1
    
    maj =  0
    c = 1
    for i in range(left+1,right):
        if a[i] == a[maj]:
            c = c+1
        else:
            c = c-1
        if c == 0:
            maj = i
            c = 1

    count = 0
    for i in range(right):
        if a[maj] == a[i]:
            count = count+1

    if count > right//2:
        return count
    #write your code here
    return -1

if __name__ == '__main__':
    n = int(input())
    a = [int(i) for i in input().split()]
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)

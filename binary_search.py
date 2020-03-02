# Uses python3
import sys

def binary_search(a, x):
    left, right = 0, len(a)-1
    while(left<=right):
        mid = (left+right)//2
        m = a[mid]
        if m == x:
            return mid
        elif m < x:
            left = mid+1
        else:
            right = mid-1
    return -1
    # write your code here

def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

if __name__ == '__main__':
    
    data1 = [int(i) for i in input().split()]
    data2 = [int(i) for i in input().split()]
    data = [*data1,*data2]
    n = data[0]
    #print(n)
    m = data[n + 1]
    #print(m)
    a = data[1 : n + 1]
    #print(a)
    
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        #print(linear_search(a, x), end = ' ')
        print(binary_search(a, x), end = ' ')

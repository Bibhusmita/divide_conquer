# Uses python3
import sys
import random

def randomized_quicksort3(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r-1)
    a[l], a[k] = a[k], a[l]
    #use partition3
    m1, m2 = partition3(a, l, r)
    randomized_quicksort3(a, l, m1);
    randomized_quicksort3(a, m2+1, r);
    #m = partition2(a, l, r)
    #randomized_quick_sort(a, l, m - 1);
    #randomized_quick_sort(a, m + 1, r);

def partition3(a, l, r):
    #write your code here
    m2 = r
    pivot = a[l]
    for i in range(l,m2):
        if a[i] > pivot:
            a[i], a[m2] = a[m2], a[i]
            m2 = m2-1

    print(a)
    
    m1 = l
    for i in range(l,m2):
        if a[i] < pivot:
            a[i], a[m1] = a[m1], a[i]
            m1 = m1+1
    return m1,m2




def partition2(a, l, r):
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


if __name__ == '__main__':
    n = int(input())
    a = [int(i) for i in input().split()]
    randomized_quicksort3(a, 0, n - 1)
    for x in a:
        print(x, end=' ')

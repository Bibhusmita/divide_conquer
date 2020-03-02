import random
def randomized_quicksort3(a, l, r):
    # print('Splitting:', arr[l:r])
    if l  >= r:
        return

    # Pivot selection; Return a random integer N such that l <= N <= r
    k = random.randint(l, r-1)
    # temp = sorted([(0,arr[0]), ((l+r)//2,arr[(l+r)//2]), (-1,arr[-1])], key = lambda x: x[1])
    # m = temp[1][0]
    a[l], a[k] = a[k], a[l]

    # partition procedure
    m1, m2 = partition3(a, l, r)

    randomized_quicksort3(a, l, m1)
    randomized_quicksort3(a, m2+1, r)

def partition3(a, l, r):
    #write your code here
    pivot = a[l]
    i = l
    m1 = l
    m2 = r
    while i <= m2:
        if a[i] < pivot:
            a[i], a[m1] = a[m1], a[i]
            m1 += 1
            i += 1
        elif a[i] > pivot:
            a[i], a[m2] = a[m2], a[i]
            m2 -= 1
        else:
            i += 1

    return m1, m2



if __name__ == '__main__':
    n = int(input())
    a = [int(i) for i in input().split()]
    randomized_quicksort3(a, 0, n - 1)
    for x in a:
        print(x, end=' ')

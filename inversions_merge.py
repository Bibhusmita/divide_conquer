def merge(l, r):
    i, j = 0, 0
    ic = 0
    seq = []
    while i < len(l) and j< len(r):
        if l[i] <= r[j]:
            seq.append(l[i])
            i += 1
        else:
            seq.append(r[j])
            ic += len(l) - i
            j += 1

    seq += l[i:]
    seq += r[j:]
        
    return seq, ic

def mergesort(a):
    global count
    if len(a) <= 1:
        return a
    mid = len(a)//2

    l = mergesort(a[:mid])
    r = mergesort(a[mid:])

    seq, i = merge(l, r)
    count += i

    return seq

if __name__ == '__main__':
    count = 0
    n = int(input())
    a = [int(i) for i in input().split()]
    mergesort(a)
    print(count)

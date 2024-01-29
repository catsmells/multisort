import random
import matplotlib.pyplot as plt
import matplotlib.animation as anim
def swap(A, i, j):
    a = A[j]
    A[j] = A[i]
    A[i] = a
def sort_bubble(arr):
    if (len(arr) == 1):
        return
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1 - i):
            if (arr[j] > arr[j + 1]):
                swap(arr, j, j + 1)
            yield arr
def insertion_sort(arr):
    if(len(arr)==1):
        return
    for i in range(1,len(arr)):
        j = i
        while(j>0 and arr[j-1]>arr[j]):
            swap(arr,j,j-1)
            j-=1
            yield arr
def qsort(arr,p,q):
    if(p>=q):
        return
    piv = arr[q]
    pivindx = p
    for i in range(p,q):
        if(arr[i]<piv):
            swap(arr,i,pivindx)
            pivindx+=1
        yield arr
    swap(arr,q,pivindx)
    yield arr
    yield from qsort(arr,p,pivindx-1)
    yield from qsort(arr,pivindx+1,q)
def selection_sort(arr):
    for i in range(len(arr)-1):
        min = i
        for j in range(i+1,len(arr)):
            if(arr[j]<arr[min]):
                min=j
            yield arr
        if(min!=i):
            swap(arr,i,min)
            yield arr
def merge_sort(arr,lb,ub):
    if(ub<=lb):
        return
    elif(lb<ub):
        mid =(lb+ub)//2
        yield from merge_sort(arr,lb,mid)
        yield from merge_sort(arr,mid+1,ub)
        yield from merge(arr,lb,mid,ub)
        yield arr
def merge(arr,lb,mid,ub):
    new = []
    i = lb
    j = mid+1
    while(i<=mid and j<=ub):
        if(arr[i]<arr[j]):
            new.append(arr[i])
            i+=1
        else:
            new.append(arr[j])
            j+=1
    if(i>mid):
        while(j<=ub):
            new.append(arr[j])
            j+=1
    else:
        while(i<=mid):
            new.append(arr[i])
            i+=1
    for i,val in enumerate(new):
        arr[lb+i] = val
        yield arr
def heapify(arr,n,i):
    largest = i
    l = i*2+1
    r = i*2+2
    while(l<n and arr[l]>arr[largest]):
        largest = l
    while(r<n and arr[r]>arr[largest]):
        largest = r
    if(largest!=i):
        swap(arr,i,largest)
        yield arr
        yield from heapify(arr,n,largest)
def heap_sort(arr):
    n = len(arr)
    for i in range(n,-1,-1):
        yield from heapify(arr,n,i)
    for i in range(n-1,0,-1):
        swap(arr,0,i)
        yield arr
        yield from heapify(arr,i,0)
def shell_sort(arr):
    sublistcount = len(arr) // 2
    while sublistcount > 0:
      for start_position in range(sublistcount):
        yield  from gap_InsertionSort(arr, start_position, sublistcount)
      sublistcount = sublistcount // 2
def gap_InsertionSort(nlist,start,gap):
    for i in range(start+gap,len(nlist),gap):
        current_value = nlist[i]
        position = i
        while position>=gap and nlist[position-gap]>current_value:
            nlist[position]=nlist[position-gap]
            position = position-gap
            yield nlist
        nlist[position]=current_value
        yield nlist
def count_sort(arr):
    max_val = max(arr)
    m = max_val + 1
    count = [0] * m
    for a in arr:
        count[a] += 1
        yield arr
    i = 0
    for a in range(m):
        for c in range(count[a]):
            arr[i] = a
            i += 1
            yield arr
        yield  arr

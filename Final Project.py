#David McNichols Trever Cramer
import random


# Create a list of arbitrary length n made up of random integers.
def randList(n):
    rList = []
    for i in range(n):
        rand = random.randint(-9999999, 9999999)
        rList.append(rand)
    return rList


# Merge Arrays helper for MergeSort
# This will merge 2 arrays

def mergep1(a1,a2):
    a3 = []
    while len(a1) !=0 and len(a2) !=0:
        if a1[0]< a2[0]:
            a3.append(a1[0])
            a1.remove(a1[0])
        else:
            a3.append(a2[0])
            a2.remove(a2[0])
    if len(a1) == 0:
        a3 += a2
    else:
        a3 += a1
    return a3


#MergeSort
def mergep2(arr):
    # Excutes Mergesort
    if len(arr) == 0 or len(arr) == 1:
        return arr
    else:
        mid = len(arr)//2
        a1 = mergep2(arr[:mid])
        a2 = mergep2(arr[mid:])
        return mergep1(a1,a2)


#QuickSort
def qsort(a1):
    low=[]
    mid=[]
    high=[]

    if len(a1)>1:
        pivot = a1[0]
        for i in a1:
            if i <pivot:
                low.append(i)
            if i == pivot:
                mid.append(i)
            if i > pivot:
                high.append(i)

        return qsort(low)+qsort(mid)+qsort(high)
    else:
        return a1


#Heapify helper for HeapSort
def hsort(a1):
    #Makes the array a heap
    length = len(a1)-1
    lowparent = length//2
    for i in range( lowparent, -1,-1):
        mDown(a1,i,length)



    for i in range(length,0,-1):
        if a1[0] > a1[i]:
            spos(a1,0,i)
            mDown(a1,0,i-1)

    return a1






#Moving helper for HeapSort
def mDown(a1,p1,p2):
    lg = 2 * p1+1
    while lg <= p2:
        if (lg<p2 ) and (a1[lg]<a1[lg+1]):
            lg += 1

        if a1[lg]>a1[p1]:
            spos(a1,lg,p1)
            p1= lg
            lg=2*p1+1
        else:
            return



#Switch position helper for HeapSort
def spos(AR, a1, a2):
    temp= AR[a1]
    AR[a1]= AR[a2]
    AR[a2]= temp


#BubbleSort
def bsort(a1):
    for num in range(len(a1)-1,0,-1):
        for i in range(num):
            if a1[i]>a1[i+1]:
                temp=a1[i]
                a1[i]=a1[i+1]
                a1[i+1]=temp


    return a1


#Insertion Sort
def isort(a1):
    for i in range(1,len(a1)):

        cv = a1[i]
        pos=i

        while pos>0 and a1[pos-1]>cv:
            a1[pos]=a1[pos-1]
            pos=pos-1

        a1[pos]=cv
    return a1

def swap(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp


def printarr(A, n):
    for i in range(n):
        print(A[i], end=' ')
    print('\n')

def partition(A, low, high, i, j):
    if high - low <= 1:
        if A[high] < A[low]:
            swap(A, high, low)
        i = low
        j = high
        return

    mid = low
    pivot = A[high]
    while mid <= high:
        if A[mid] < pivot:
            swap(A, low, mid)
            low += 1
            mid += 1
        elif A[mid] == pivot:
            mid += 1
        elif A[mid] > pivot:
            swap(A, mid, high)
            high -= 1

    i = low - 1
    j = mid
    

def quickSort(A, low, high):
    if low >= high:
        return
    i = low
    j = high

    partition(A, low, high, i, j)
    quickSort(A, low, i)
    quickSort(A, j, high)


arr = []

num = int(input('Enter the number of elements in the list : '))
print('Enter the elements in the list : ')

for i in range(num):
    ele = int(input())
    arr.append(ele)

size = len(arr)
print('Entered array : \n')
printarr(arr, size)

quickSort(arr, 0, size - 1)
print('Sorted array after three way partitioning:\n')
printarr(arr, size)

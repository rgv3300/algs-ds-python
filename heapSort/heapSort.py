def heapify(arr, n , i):
    largest = i
    left = i * 2
    right = i * 2 + 1

    if left < n and arr[largest] < arr[left]:
        largest = left

    if right < n and arr[largest] < arr[right]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]

        heapify(arr, n, largest)


def heapSort(arr):
    n = len(arr)

    for i in range(n//2 - 1, -1, -1):
        heapify(arr,n,i)

    for i in range(n-1,0,-1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr,i,0)

arr = [23, 234, 23, 56,31, 11, 456,6 ,8 ]

heapSort(arr)

n = len(arr)

print("Sorted array is : ")
for i in range(n):
    print("%d" % arr[i])

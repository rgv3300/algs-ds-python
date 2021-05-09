import timeit

a ='''  
def insertion_sort_recursive(arr,n):
    if n > 1:
        insertion_sort_recursive(arr,n-1)
    key = arr[n-1]
    j = n-2
    while j>=0 and arr[j]>key:
        arr[j+1] = arr[j]
        j -= 1
    arr[j+1] = key


data = [72, 10, 39, 18, 78, 94, 47, 70, 82, 14, 44, 17, 22, 20, 86, 63, 53, 26, 61, 19, 29, 62, 85, 68, 73, 45, 50, 16, 91, 98, 83, 21, 57, 58, 13, 48, 64, 6, 7, 77, 8, 25, 24, 84, 89, 55, 79, 65, 46, 33, 27, 5, 99, 35, 34, 97, 28, 30, 93, 42, 23, 88, 51, 75, 96, 76, 9, 3, 52, 36, 15, 60, 4, 12, 100, 80, 32, 31, 69, 66, 87, 92, 54, 81, 71, 74, 1, 49, 90, 11, 38, 59, 41, 37, 67, 56, 95, 40, 43, 2]

insertion_sort_recursive(data,len(data))
'''
print("time taken is ", timeit.timeit(stmt= a, number = 1000))

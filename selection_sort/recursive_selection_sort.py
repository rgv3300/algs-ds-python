import timeit

a = '''
def min_idx(arr,i,j):
    if i == j:
        return i

    k = min_idx(arr, i+1, j)

    return(i if arr[i] < arr[k] else k)


def recursive_selection(arr,n,i=0):
    if n == i:
        return
    k = min_idx(arr,i,n-1)

    if k!= i:
        a[k],a[i] = a[i],a[k]


    recursive_selection(arr,n,i+1)


arr = [3,1,5,2,7,0]

recursive_selection(arr,len(arr))'''

print("time taken is: ",timeit.timeit(stmt = a, number = 1))

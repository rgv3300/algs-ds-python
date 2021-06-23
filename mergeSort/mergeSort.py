def mergeSort(array):
    if len(array) > 1:

        m = len(array)//2

        l = array[:m]
        r = array[m:]

        mergeSort(l)
        mergeSort(r)

        i = j = k = 0

        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                array[k] = l[i]
                i += 1
            else:
                array[k] = r[j]
                j += 1
            k += 1

        while i < len(l):
            array[k] = l[i]
            i += 1
            k += 1

        while j < len(r):
            array[k] = r[j]
            j += 1
            k += 1


array = [7,2,9,34,8,2,5,92]
print(array)
mergeSort(array)

print(array)

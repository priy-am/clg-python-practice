# WAP for sorting algorithms: 
# i. Bubble sort 
def bubbleSort(arr):
    n = len(arr)
    for i in range( n-1):
        for j in range(n-i-1):
            if(arr[j]>arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
# ii.insertion sort using list
def insertionSort(arr):
    n = len(arr)
    for i in range(1, n-1):
        key = arr[i]
        j = i-1  # to check the previous element 
        while j >= 0 and key < arr[j]:
            arr[j+1 ] = arr[j]
            j -= 1
        arr[j+1]= key
    return arr




arr = [ 53, 256, 2563, 254, 23, 89, 99]
sorted_arr = bubbleSort(arr)
print("sorted list by using bubble shorting ", sorted_arr)
sorted_arr2 = insertionSort(arr)
print("sorted list by using insertion shorting ", sorted_arr2)



# QuickSort - Pythonic
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

#print(quicksort([3,6,8,10,1,2,1]))


# QuickSort - Normal
def partition(start, end, arr):
    """Returns the partition index."""
    # Last element chosen as Pivot
    pivot = arr[end]
    p_index =  start
    for i in range(start, end): #Places pivot in correct position
        if arr[i] <= pivot:
            # Swap arr[i] with arr[p_index]
            arr[i], arr[p_index] = arr[p_index], arr[i]
            p_index += 1

    # Swapping the pivot element with element at p_index
    arr[p_index], arr[end] = arr[end], arr[p_index]
    return p_index
    

def quicksort(start, end, arr):
    if start < end:
        p_index = partition(start, end, arr)
        quicksort(start, p_index-1, arr)
        quicksort(p_index+1, end, arr)


arr = [1,5,-9,6,-66,-70,2,45]
quicksort(0,len(arr)-1,arr)
print(arr)


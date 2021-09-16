# Bubble Sorting Algorithm - Inplace and Stable sorting algorithm

arr = [6,1,5,-9,2,12,4,0]
#arr = [1,2,3,4,5,6]
n = len(arr)
isSwapped = 0
for i in range(1,n):
    # This loop will move the max element of the left unsorted part to it's
    # correct position.
    for j in range(n-1):
        if arr[j] > arr[j+1]:
            # Swapping
            arr[j+1], arr[j] = arr[j], arr[j+1]
            isSwapped = 1
    print(f'After Iteration - {i}: {arr}')
    # If not swapped, then the array is already sorted
    if not isSwapped:
        break
        

print(f'\nAfter Sorting: {arr}')

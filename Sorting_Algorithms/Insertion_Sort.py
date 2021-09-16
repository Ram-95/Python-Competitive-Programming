# Insertion Sort - Inplace and Stable
arr = [2,4,1,5,0,65,-9]
n = len(arr)
print(f'Before Sorting: {arr}')    
for i in range(1,n):
    val, curr_idx = arr[i], i
    # Moving all the elements of sorted part to their appropriate position
    while curr_idx > 0 and arr[curr_idx - 1] > val:
        arr[curr_idx] = arr[curr_idx-1]
        curr_idx -= 1

    arr[curr_idx] = val



print(f'After Sorting: {arr}')    

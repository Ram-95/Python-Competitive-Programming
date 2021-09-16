# Selection Sort Algorithm - Inplace and Unstable
arr = [2,4,1,6,7,9]
n = len(arr)
print(f'Before Sorting: {arr}')    
for i in range(n):
    idx = i
    for j in range(i+1, n):
        if arr[j] < arr[idx]:
            idx = j
    # Swapping the numbers
    arr[i], arr[idx] = arr[idx], arr[i]

print(f'After Sorting: {arr}')    
        

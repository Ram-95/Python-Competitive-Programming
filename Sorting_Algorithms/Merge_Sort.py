# Merge Sorting Algorithm
arr = [2,4,1,-9,5,32,-55]

def merge(l: list, r: list, arr: list) -> None:
    i,j,k= 0,0,0
    while i<len(l) and j<len(r):
        if l[i] < r[j]:
            arr[k] = l[i]
            i += 1
        else:
            arr[k] = r[j]
            j += 1

        k += 1

    while i<len(l):
        arr[k] = l[i]
        k += 1
        i += 1

    while j < len(r):
        arr[k] = r[j]
        k += 1
        j += 1


def mergesort(arr: list, n: int):
    if n < 2:
        return
    mid = n//2
    # Left sublist
    l = arr[:mid]
    # Right sublist
    r = arr[mid:]
    # Call mergesort on the left sublist
    mergesort(l, len(l))
    # Call mergesort on the right sublist
    mergesort(r, len(r))
    # Merge both the left and right sublist into the original array
    merge(l,r, arr)

# Driver Code
mergesort(arr, len(arr))
print(f'After Sorting: {arr}')

#Stock Span
def solve(arr, n):
    #Stack - Stores the (element,index) of the element in the array
    st = []
    ans = [None] * n

    #Storing the index of the first element of the array
    ans[0] = 1

    for i in range(1,n):
        count = 1
        while len(st) > 0 and st[-1][0] <= arr[i]:
            count += st.pop()[1]
        st.append((arr[i],count))
        ans[i] = count

    return ans
        

arr = [100, 80, 60, 70, 60, 75, 85]
print(solve(arr, len(arr)))

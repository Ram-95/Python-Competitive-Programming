#list Comparison

def compare_lists(a,b):
    (sa,sb) = (0,0)
    total_list = [0,0]
    for i in range(3):
        if a[i] > b[i]:
            sa = sa + 1
        elif a[i] < b[i]:
            sb = sb + 1
        else:
            continue

    total_list[0] = sa
    total_list[1] = sb

    return total_list
    

a = [5,4,8]
b = [7,1,3]
print(compare_lists(a,b))

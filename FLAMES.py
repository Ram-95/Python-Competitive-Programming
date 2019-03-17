#FLAMES Game --- Incomplete

def flames(l, n):
    while( len(l) > 1 ):
        split_index = n % len(l) - 1

        if split_index >= 0:
            right = l[split_index + 1: ]
            left = l[:split_index]
            l = right + left
        else:
            l = l[: len(l) - 1]

    return (l[0])



flames_l = ['Friends','Lovers','Acquaintance','Marriage','Enemies','Siblings']


l = (input('Enter first name: '))

l1 = (input('Enter Second name: '))

common_list = list(set(l) ^ set(l1))

key = len(common_list)

print('{} and {} are: {}'.format(l,l1,flames(flames_l, key)))
    

    

    
        




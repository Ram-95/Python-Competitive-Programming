#Tale of Two Lands - CodeForces
def TaleofTwo(a,b):
    count = 0
    #array_land = abs(a - b) + 1
    v_a = abs(a - b)
    v_b = abs(a + b)

    #Finding the absolute values of a and b
    a = abs(a)
    b = abs(b)

    if v_a < v_b:
        if (a in range(v_a, v_b + 1)) and (b in range(v_a, v_b + 1)):
            count = count + 1
    elif v_a >= v_b:
        if (a in range(v_b, v_a + 1)) and (b in range(v_b, v_a + 1)):
            count = count + 1
        
      
    return count
    
        


n = int(input())

xyz = list(map(int, input().rstrip().split()))

print(TaleofTwo(arr))
        


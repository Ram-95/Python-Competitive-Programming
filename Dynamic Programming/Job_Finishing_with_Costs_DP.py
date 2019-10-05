#Finishing the jobs in minimum time. Switching jobs comes with an additional cost
'''
Find the min. time taken to finish all the jobs. Any job can be performed by any
machine but there is an additional cost when we switch to other machines

Machines: A and B
C - Additional cost when switched from A->B or B->A

A: [10,3,8,12,15]
B: [4,15,6,2,9]
'''


#Inputs
n = int(input('Enter N {Jobs}: '))
print('Enter the Time Taken to finish each job by A/B:')
A = list(map(int, input().rstrip().split()))
B = list(map(int,input().rstrip().split()))
c = int(input('Cost of Switching: '))


'''Precomputation of DP Tables'''
#Table Size
dpA = [0] * n
dpB = [0] * n

#Base Conditions
dpA[0] = A[0]
dpB[0] = B[0]


#Computing Dp Tables
for i in range(1, n):
    dpA[i] = min(dpA[i-1], dpB[i-1]+c) + A[i]
    dpB[i] = min(dpB[i-1], dpA[i-1]+c) + B[i]

    
#Answer
print(min(dpA[n-1], dpB[n-1]))

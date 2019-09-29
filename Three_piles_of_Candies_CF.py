#Three piles of candies - Codeforces A

def three_piles(arr, n):
    return sum(arr)//2
    



q = int(input())
while q:
    arr = list(map(int, input().rstrip().split()))
    print(three_piles(arr, len(arr)))
    q = q - 1

#From Hero to Zero


def hero_to_zero(n,k):
    count = 0
    while n:
        nex = (n//k) * k
        count = count + (n - nex)
        n = n - (n-nex)

        while(n and n%k == 0):
            n = n // k
            count += 1

    return count


t = int(input())
while t:
    nk = list(map(int, input().rstrip().split()))
    n = nk[0]
    k = nk[1]
    print(hero_to_zero(n,k))
    t = t - 1

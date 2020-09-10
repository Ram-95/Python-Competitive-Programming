class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        n = len(secret)
        ds, dg = collections.defaultdict(int), collections.defaultdict(int)
        bulls, cows = 0, 0
        for i in range(n):
            if secret[i] == guess[i]:
                bulls += 1
            else:
                ds[secret[i]] += 1
                dg[guess[i]] += 1
        
        for item in dg:
            cows += min(dg[item], ds[item])
             
        return str(bulls) + 'A' + str(cows) + 'B'
        

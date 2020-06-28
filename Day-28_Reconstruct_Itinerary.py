class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        d = collections.defaultdict(list)
        
        for i,j in sorted(tickets)[::-1]:
            d[i] += j,
        
        ans = []    
        def solve(a):
            while d[a]:
                solve(d[a].pop())
                
            ans.append(a)
        solve("JFK")
        
        return ans[::-1]
            
        


            
            

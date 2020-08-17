class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        arr = [0] * num_people
        # Index to traverse the array
        idx = 0
        # Starting with 1 chocolate
        chocs = 1
        while candies > 0:
            # Add up the minimum of available candies and chocs so far
            arr[idx % num_people] += min(chocs, candies)
            # To handle the case where No.of candies becomes negative
            candies -= min(chocs, candies)
            idx += 1
            # Add 1 to the previously given candy
            chocs += 1
            
        return arr
        

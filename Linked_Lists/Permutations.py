class Solution:
    def permute(self, arr: List[int]) -> List[List[int]]:
        if len(arr) == 0:
            return []
        elif len(arr) == 1:
            return [arr]
        else:
            ans = []
            for i in range(len(arr)):
                curr_elem = arr[i]
                # Remaining elements before and after curr_elem as list
                rem = arr[:i] + arr[i+1:]
                # Generate permutations of the remaining
                for el in self.permute(rem):
                    ans.append([curr_elem] + el)
            
            return ans

'''Question: Given a non-empty array of integers, return the k most frequent elements.'''


'''My Initial Solution - Time O(NlogN)'''
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a = Counter(nums)
        #Sorting the dictionary based on the Value
        a = {k: v for k, v in sorted(a.items(),key= lambda x: x[1],reverse=True)}
        #print(a)
        return list(a.keys())[:k]
        


'''Using Heaps nlargest function - Time O(NlogK)'''
from heapq import nlargest
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums):
            return nums
        
        a = Counter(nums)
        print(a)
        return nlargest(k, a.keys(), key=a.get)
  
  
  
  ''' Using Hoare's Selection Algorithm - Time O(N)'''
  # Read at: https://leetcode.com/articles/top-k-frequent-elements/
  
  def partition(left, right, pivot_index) -> int:
    pivot_frequency = count[unique[pivot_index]]
    # 1. move pivot to the end
    unique[pivot_index], unique[right] = unique[right], unique[pivot_index]  
    
    # 2. move all less frequent elements to the left
    store_index = left
    for i in range(left, right):
        if count[unique[i]] < pivot_frequency:
            unique[store_index], unique[i] = unique[i], unique[store_index]
            store_index += 1

    # 3. move pivot to its final place
    unique[right], unique[store_index] = unique[store_index], unique[right]  
    
    return store_index

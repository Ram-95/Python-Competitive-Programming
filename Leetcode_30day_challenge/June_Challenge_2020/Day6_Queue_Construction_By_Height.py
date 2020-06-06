class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        n = len(people)
        #List to store the answer
        ans = [] * n
        
        #Sorting the given list -> Increasing order of Height [H] and then by decreasing order of K
        people.sort(key=lambda x: (-x[0], x[1]))
        
        #Inserting the Elements of sorted people list, at indexes 'k'
        for i in people:
            ans.insert(i[1], i)
        
        return ans

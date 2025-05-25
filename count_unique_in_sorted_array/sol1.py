class Solution:
    def __init__(self,nums):
        self.nums=nums
    
    def count_unique(self):
        if not self.nums:
            return "Empty list"
        seen=set()
        unique=[]
        for num in self.nums:
            if num not in seen:
                unique.append(num)
                seen.add(num)
        return len(unique)


nums=[1,1,2,2,3,3,4]
# nums=[]
sol=Solution(nums)
print(sol.count_unique())

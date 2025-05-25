class Solution:
    def __init__(self,nums):
        self.nums=nums
    
    def count_unique(self):
        if not self.nums:
            return "Empty list"
        unique=[]
        for num in self.nums:
            if num not in unique:
                unique.append(num)

        return len(unique)


nums=[1,1,2,2,3,3,4]
# nums=[]
sol=Solution(nums)
print(sol.count_unique())

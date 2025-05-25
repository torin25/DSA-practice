class Solution:
    def __init__(self,nums):
        self.nums=nums

    def reverse_array(self):
        if not self.nums:
            return "Empty array"
        
        if len(self.nums)==1:
            return self.nums
        
        n=len(self.nums)
        for i in range(n//2):
            self.nums[i], self.nums[n-1-i]=self.nums[n-1-i], self.nums[i]

        return self.nums

nums=[1,2,3,4,5]
# nums=[]
sol=Solution(nums)
print(sol.reverse_array())
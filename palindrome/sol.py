class Solution:
    def __init__(self,nums):
        self.nums=nums
    
    def check_palindrome(self):

        if not self.nums:
            return "Empty array"
        
        n=len(self.nums)
        for i in range(n//2):
            if self.nums[i]!=self.nums[n-1-i]:
                return False
        
        return True
nums=[1,2,3,2,1]
sol=Solution(nums)
print(sol.check_palindrome())
class Solution:
    def __init__(self,nums):
        self.nums=nums
    def sort_squares(self):
        n=len(self.nums)
        left=0
        right=n-1
        result=[0]*n
        index=n-1
        while left<=right:

            left_sq=self.nums[left]**2
            right_sq=self.nums[right]**2

            if left_sq>right_sq:
                result[index]=left_sq
                left+=1
            else:
                result[index]=right_sq
                right-=1
            index-=1
            
        return result
        
nums=[-4,-1,0,3,10]  
sol=Solution(nums)
print(sol.sort_squares())

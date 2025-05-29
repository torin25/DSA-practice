class Solution:
    def single_number(self,nums):
        result=0
        for num in nums:
            result^=num
            print(result)
        

nums=[4,1,2,1,2]
sol=Solution()
print(sol.single_number(nums))
class Solution:
    def majority_element(self,nums):
        n=len(nums)
        count={}
        for num in nums:
            count[num]=count.get(num,0)+1
        
        for num in count:
            if count[num]>n//2:
                return num


nums=[3,2,3]
sol=Solution()
print(sol.majority_element(nums))
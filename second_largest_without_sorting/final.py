class Solution:
    def secondLargestElement(self, nums):
        
        if not nums:
            return -1
        if len(set(nums))==1:
            return -1
        
        
        largest=nums[0]
        second=float("-inf")
        for num in nums:
            if num>largest:
                second=largest
                largest=num
            elif num<largest and num>second:
                second=num

        if second==float("-inf"):
            return -1
        return second

nums=nums = [10, 10, 10, float("-inf")]

              
sol=Solution()
print(sol.secondLargestElement(nums))
class Solution():
    def secondLargestElement(self,nums):
        if not nums:
            return -1
        if len(set(nums))==1:
            return -1
        
        largest=nums[0]
        large_second_diff=float('inf')

        for num in nums:
            if num>largest:
                largest=num

        for i in range(len(nums)):
            nums[i]=largest-nums[i]


        for num in nums:
            if num<large_second_diff:
                if num!=0:
                    large_second_diff=num
                    
        if (largest-large_second_diff) ==float("-inf"):
            return -1

        return  (largest-large_second_diff)     

nums=[10, 10, 10, float("-inf")]

              
sol=Solution()
print(sol.secondLargestElement(nums))
class Solution:
    def bubble_sort(self,nums):
        n=len(nums)
        for i in range(n-1,0,-1):
            did_swap=0
            for j in range(0,i):
                if nums[j]>nums[j+1]:
                    nums[j],nums[j+1]=nums[j+1],nums[j]
                    did_swap=1

            if did_swap==0:
                break
            
        return nums


nums = [5,4,3,2,1,]

sol=Solution()
print(sol.bubble_sort(nums))
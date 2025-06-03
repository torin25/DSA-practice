class Solution:
    def bubble_sort(self,nums):
        n=len(nums)
        for i in range(n-1,0,-1):
            for j in range(0,i):
                if nums[j]>nums[j+1]:
                    nums[j],nums[j+1]=nums[j+1],nums[j]
        return nums


nums = [5, 4, 4, 1, 1]

sol=Solution()
print(sol.bubble_sort(nums))
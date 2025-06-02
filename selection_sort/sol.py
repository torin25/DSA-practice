class Solution:
    def selection_sort(self,nums):
        n=len(nums)
        for i in range(n-1):
            min_index=i
            for j in range(i,n):
                if nums[j]<nums[min_index]:
                    min_index=j
            nums[i],nums[min_index]=nums[min_index],nums[i]

        return nums

nums = [7, 4, 1, 5, 3]
sol=Solution()
print(sol.selection_sort(nums))
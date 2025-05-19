from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        i=0

        max_range=[]
        while i<len(nums):
            j=i

            while j+1<len(nums) and nums[j+1]==nums[j]+1:
                j+=1
            l_range=list(range(nums[i],nums[j]+1))

            if l_range==nums[i:j+1]:
                if nums[i]!=nums[j]:
                    max_range.append(f"{nums[i]}->{nums[j]}")
                else:
                    max_range.append(f"{nums[i]}")

            i=j+1

        return max_range
               
# print(Solution().summaryRanges([0,1,2,4,5,7]))
# It prints ['0->2', '4->5', '7']
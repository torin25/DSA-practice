from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        # Prefix-Suffix method

        prefix=[1]*n
        suffix=[1]*n
        answer=[1]*n

        for i in range(1,n):
            prefix[i]=prefix[i-1]*nums[i-1]

        for i in range(n-2,-1,-1):
            suffix[i]=suffix[i+1]*nums[i+1]

        for i in range(n):
            answer[i]=prefix[i]*suffix[i]

        return answer
    
print(Solution().productExceptSelf(nums=[-1,1,0,-3,3]))
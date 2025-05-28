# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]

class Solution:
    def rotate_array(self,nums,k):
        k%=len(nums)
        if len(nums)==1:
            return 

        if k==0:
            return
        nums[:]=nums[-k:]+nums[:-k]

        return nums
# nums=[1,2,3,4,5,6,7]
# k=3
nums = [-1,-100,3,99]
k = 2
sol=Solution()
print(sol.rotate_array(nums,k))

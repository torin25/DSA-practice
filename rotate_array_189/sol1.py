# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]

class Solution:
    def rotate_array(self,nums,k):
        result=nums[-k:]+nums[:len(nums)-k]
        return result


nums=[1,2,3,4,5,6,7]
k=3
# nums = [-1,-100,3,99]
# k = 2
sol=Solution()
print(sol.rotate_array(nums,k))

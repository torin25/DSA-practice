class Solution:
    def missing_num(self,nums):
        n=len(nums)
        nums_set=set(nums)
        range_set=(set(range(n+1)))
        for char in (range_set-nums_set):
            return char


nums=[9,6,4,2,3,5,7,0,1]
sol=Solution()
print(sol.missing_num(nums))
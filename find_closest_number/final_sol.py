class Solution:
    def findClosestNumber(self, nums):
        closest = nums[0]
        for num in nums:
            if abs(num) < abs(closest) or (abs(num) == abs(closest) and num > closest):
                closest = num
        return closest


nums=list(map(int,input("").split(" ")))

sol=Solution()
print(sol.findClosestNumber(nums))
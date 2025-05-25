class Solution:
    def __init__(self,nums):
        self.nums=nums

    def zeroes_end(self):
        k=0
        for i in range(len(self.nums)):
            if self.nums[i]!=0:
                self.nums[k]=self.nums[i]
                k+=1
        
        for i in range(k,len(self.nums)):
            self.nums[i]=0

        return self.nums

nums = [0,1,0,0,3,12]     
sol=Solution(nums)
print(sol.zeroes_end())
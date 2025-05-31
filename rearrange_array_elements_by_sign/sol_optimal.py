class Solution:
    def rearrange(self,nums):
        result=[0]*len(nums)
        pos,neg=0,1
        for num in nums:
            if num>0:
                result[pos]=num
                pos+=2
            else:
                result[neg]=num
                neg+=2
        return result

nums=[-1,1]
sol=Solution()
print(sol.rearrange(nums))
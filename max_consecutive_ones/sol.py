# nums = [1,1,0,1,1,1,2,3,4,1,1,1,1,2,3]
nums=[1,1,1,1,1,]

class Solution:
    def count_max(self,nums):
        if not nums:
            return 0
        k=0
        ones_list=[]
        for i in range(len(nums)):
            if nums[i]==1:
                k+=1
            
            else:
                ones_list.append(k)
                k=0

        ones_list.append(k)

        return max(ones_list)

sol=Solution()
print(sol.count_max(nums))
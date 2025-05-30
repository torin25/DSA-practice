class Solution:
    def two_sum(self,nums,target):
        num_to_index={}

        for index,num in enumerate(nums):
            compliment=target-num
            if compliment in num_to_index:
                return[num_to_index[compliment],index]
            num_to_index[num]=index
            


nums=[3,4,0]
target=3
sol=Solution()
print(sol.two_sum(nums,target))
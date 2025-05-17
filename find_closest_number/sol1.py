class Solution(object):
    def findClosestNumber(self, nums):
        dist_num=[abs(num) for num in nums]
        ans=min(dist_num)
        nums_index=[i for i in range(len(dist_num)) if dist_num[i]==ans]
        check_ans=[nums[num_index] for num_index in nums_index]
        return max(check_ans)
        
nums=list(map(int,input("").split(" ")))

sol=Solution()
print(sol.findClosestNumber(nums))
        
        
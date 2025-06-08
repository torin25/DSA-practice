class Solution:
    def lcs(self,nums):
        count_list=[]
        count=1
        n=len(nums)

        # if bubble sort is used, then the time limit exceeds in case of a large input size.
        # for i in range(n-1,0,-1):
        #     for j in range(0,i):
        #         if nums[j]>nums[j+1]:
        #             nums[j],nums[j+1]=nums[j+1],nums[j]

        nums.sort()
        
        for i in range(n-1):
            if nums[i+1]==nums[i]+1:
                count+=1
            elif nums[i+1]!=nums[i]:
                count_list.append(count)
                count=1
                
        count_list.append(count)

        
        return max(count_list)

        # max=count_list[0]
        # for num in count_list:
        #     if num>max:
        #         max=num
        # return max
            
       
nums = [1,0,1,2]     
sol=Solution()
print(sol.lcs(nums))
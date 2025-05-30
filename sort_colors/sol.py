class Solution:
    def sort_colors(self,nums):
        count={}

        for num in nums:
            if num in count:
                count[num]+=1
            else:
                count[num]=1
        
        def recursive_placing(start,end,value):
            for i in range(start,end):
                nums[i]=value
        
        recursive_placing(0,count[0],value=0)
        recursive_placing(count[0],count[0]+count[1],value=1)
        recursive_placing(count[0]+count[1],count[0]+count[1]+count[2],value=2)

        return nums


nums=[2,0,1,1,2,0,1,2]   
sol=Solution()
print(sol.sort_colors(nums))
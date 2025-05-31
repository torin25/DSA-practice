class Solution:
    def sort_colors(self,nums):
        count={}

        for num in nums:
            count[num]=count.get(num,0)+1

        def recursive_placing(start,end,value):
            for i in range(start,end):
                nums[i]=value

        recursive_placing(0,count.get(0,0),value=0)
        recursive_placing(count.get(0,0),count.get(0,0)+count.get(1,0),value=1)
        recursive_placing(count.get(0,0)+count.get(1,0),count.get(0,0)+count.get(1,0)+count.get(2,0),value=2)

        return nums

nums=[1,2,2,1,2]
sol=Solution()
print(sol.sort_colors(nums))
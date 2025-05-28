class Solution:
    def rotate_array(self,nums,k):
        n=len(nums)

        def reverse(start,end):
            while start<=(start+end)//2:
                nums[start],nums[end]=nums[end],nums[start]
                start+=1
                end-=1
                

        reverse(0,n-1)
        reverse(0,(k-1)%n)
        reverse(k%n,n-1)

        return nums
    
# nums=[1,2,3,4,5,6,7]
# k=3
nums = [1,2,3]
k = 4
sol=Solution()
print(sol.rotate_array(nums,k))

        

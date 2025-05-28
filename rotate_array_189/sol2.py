class Solution:
    def rotate_array(self,nums,k):
        n=len(nums)
        if n==1:
            return
        if k==n:
            return
        
        i,j=0,len(nums)-1
        while i<n//2:
            nums[i],nums[j]=nums[j],nums[i]
            i+=1
            j-=1

        i,j=0,(k-1)%n
        while i<k//2:
            nums[i],nums[j]=nums[j],nums[i]
            i+=1
            j-=1
            
        i,j=k%n,n-1
        while i<(n+k)//2:
            nums[i],nums[j]=nums[j],nums[i]
            i+=1
            j-=1
        
        
        return nums

        
nums=[1,2,3,4,5,6,7]
k=3
# nums = [-1,-100,3,99]
# k = 2
sol=Solution()
print(sol.rotate_array(nums,k))
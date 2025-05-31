class Solution:
    def rearrange(self,nums):
        n=len(nums)
        segregate=[0]*n
        result=[0]*n
        j,k=0,n//2
        
        for i in range(n):
            if nums[i]>0:
                segregate[j]=nums[i]
                j+=1
            else:
                segregate[k]=nums[i]
                k+=1

        j,k=0,n//2
        for i in range(n):
            if i%2==0:
                result[i]=segregate[j]
                j+=1
            else:
                result[i]=segregate[k]
                k+=1
        return result
                

nums = [-1,1]    
sol=Solution()
print(sol.rearrange(nums))

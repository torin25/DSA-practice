class Solution:
    def next_permutation(self,nums):
        
        n=len(nums)
        for i in range(n-1,0,-1):
            if nums[i-1]<nums[i]:
                break

        else:
            nums.sort()
            return nums

        for j in range(n-1,i-2,-1):
            if nums[j]>nums[i-1]:
                nums[j],nums[i-1]=nums[i-1],nums[j]
                break
        # approach-1
        # start=i
        # end=n-1
        # print(i)
        # while start<((n-1)+i)//2:
        #     nums[start],nums[end]=nums[end],nums[start]
        #     start+=1
        #     end-=1

        # approach-2 : using reversed() function
        # nums[i:]=reversed(nums[i:])

        # approach-3
        nums[i:]=nums[i:][::-1]
        return nums

nums=[1,2,3]
sol=Solution()
print(sol.next_permutation(nums))








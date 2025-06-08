class Solution:
    def set_matrix_zeroes(self,nums):
        n1=len(nums)
        n2=len(nums[0])
                
        zeroes=[]
        for i in range(n1):
            for j in range(n2):
                if nums[i][j]==0:
                    zeroes.append([i,j])
        
        for zero in zeroes:
            nums[zero[0]]=[0]*n2

            for i in range(n1):
                nums[i][zero[1]]=0
              
        return nums


nums=[[1,1,1],
      [1,0,1],
      [1,1,1]]

# nums=[[0,1,2,0],
#       [3,4,5,2],
#       [1,3,1,5]]

sol=Solution()
print(sol.set_matrix_zeroes(nums))
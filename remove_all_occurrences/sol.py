class Solution:
        def __init__(self,nums, target):
            self._nums=nums
            self._target=target
        
        def remove_target(self):
            k=0
            for i in range(len(self._nums)):
                if self._nums[i]!=self._target:
                    self._nums[k]=self._nums[i]
                    k+=1
            
            for i in range(k,len(self._nums)):
                 self._nums[i]="_"
            return k,self._nums

nums=[1,2,3,2,4]
target=2
sol=Solution(nums,target)
print(sol.remove_target())


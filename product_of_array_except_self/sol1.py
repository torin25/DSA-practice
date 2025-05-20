import math
nums=[-1,1,0,-3,3]
i=0
answer=[]
while i<len(nums):
    mul_list=nums[0:i]+nums[i+1:]
    answer.append(math.prod(mul_list))
    i+=1

print(answer)
class Solution:
    def merge_arrays(self,nums1,nums2,m,n):
        if not nums2:
            return nums1

        if nums1[m-1]<=nums2[0]:
            j=0
            for i in range(m,m+n):
                nums1[i]=nums2[j]
                j+=1
            return nums1
        
        i=m-1
        j=n-1
        k=m+n-1
        while j>=0:
            if nums1[i]>nums2[j]:
                nums1[k]=nums1[i]
                i-=1
            else:
                nums1[k]=nums2[j]
                j-=1
            k-=1

        
        return nums1
            
n1=[1,2,3,7,9,0,0,0]
m=5
n2=[1,5,6]   
n=3   
sol=Solution()
print(sol.merge_arrays(n1,n2,m,n))
class Solution:
    def first_unique_char(self,word):
        if not word:
            return "Empty string"
        
        dict={}
        for char in word:
            
            if char in dict:
                dict[char]+=1
            else:
                dict[char]=1


        for i,char in enumerate(word):
            if dict[char]==1:
                return i
        
        return -1


# word="lleettccoodde"
word="leetcode"
sol=Solution()
print(sol.first_unique_char(word))
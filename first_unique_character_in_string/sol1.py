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
        # print(dict)

        first_unique_char=""
        for char,count in dict.items():
            if count==1:
                first_unique_char=char
                break
        
        if first_unique_char=="":
            return -1


        for i in range(len(word)):
            if word[i]==first_unique_char:
                return i


# word="lleettccoodde"
word="leetcode"
sol=Solution()
print(sol.first_unique_char(word))
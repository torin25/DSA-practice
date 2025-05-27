class Solution:
    def check_anagram(self,s,t):
        if len(s)!=len(t):
            return False
        dict_s={}
        dict_t={}
        n=len(s)
        for char in s:
            if char in dict_s:
                dict_s[char]+=1
            else:
                dict_s[char]=1
        
        for char in t:
            if char in dict_t:
                dict_t[char]+=1
            else:
                dict_t[char]=1
        if dict_t==dict_s:
            return True
        
        return False

# s="anagram"
# t="nagaram"
s=""
t=""
sol=Solution()
print(sol.check_anagram(s,t))
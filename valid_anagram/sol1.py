from collections import Counter

class Solution:
    def check_anagram(self, s, t):
        return Counter(s) == Counter(t)

s="anagram"
t="nagaram"
# s=""
# t=""
sol=Solution()
print(sol.check_anagram(s,t))
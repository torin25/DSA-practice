class Solution:
    def romanToInt(self, roman: str) -> int:
        dict={"I":1,
                    "V":5,
                    "X":10,
                    "L":50,
                    "C":100,
                    "D":500,
                    "M":1000}

        val=0
        char_list=[]
        for char in roman:
            char_list.append(char)



        i=0  
        while i<len(char_list):
            if ( i+1<len(char_list) and 
                (char_list[i]=="I" and char_list[i+1] in ("V" , "X") or 
                char_list[i]=="X" and char_list[i+1] in ("L" , "C") or 
                char_list[i]=="C" and char_list[i+1] in ("D" , "M"))):

                val+=(dict[char_list[i+1]]-dict[char_list[i]])
                i+=2

            else:
                val+=dict[char_list[i]]
                i+=1

        return val

sol=Solution()
print(sol.romanToInt(input("")))
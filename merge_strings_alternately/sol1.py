def merge(word1, word2):
    final_str=""
    i,j=0,0
    if len(word1)==len(word2):
        
        while i<len(word1) and j<len(word2):
            final_str+=word1[i]+word2[j]
            i+=1
            j+=1

        return final_str
    
    elif len(word1)<len(word2):
        while i<len(word1):
            final_str+=word1[i]+word2[i]
            i+=1
        final_str+=word2[len(word1):]
        return final_str
    else:
        i=0
        while i<len(word2):
            final_str+=word1[i]+word2[i]
            i+=1
        final_str+=word1[len(word2):]
        return final_str



sol=merge("abc","pqr")
print(sol)
          
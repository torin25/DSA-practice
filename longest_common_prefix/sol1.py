string=["car","cir"]

def func(string):
    if not string:
        return ""
    
    else:
        prefix=""
        for i in range(len(string[0])):
            current_char=string[0][i]
            if all(i<len(word) and current_char==word[i] for word in string[1:] ):
                prefix+=current_char
            
        return prefix
           
    return string[0]

print(func(string))


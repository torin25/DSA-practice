def longest_common_prefix(string):
    if not string:
        return ""

    else:
        
        for i in range(len(string[0])):
            current_char=string[0][i]

            for word in string[1:]:
                if i>=len(word) or current_char!=word[i]  :
                    return string[0][:i]

    return string[0]


def main():
    string=[]
    n=int(input("Enter the number of strings you want to input:"))
    for i in range(n):
        string.append(input(f"Enter string {i+1}: "))

    print(f"The longest common prefix amongst this array of strings is: {longest_common_prefix(string)}")

main()
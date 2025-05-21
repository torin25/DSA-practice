matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[7,4,1],[8,5,2],[9,6,3]]

i,j=0,0
first=0
last=len(matrix)-1

ans = [[0]*len(matrix) for _ in range(len(matrix))]
while i<len(matrix) and j<len(matrix) and first<len(matrix) and last>=0:
    
    ans[i][j]=matrix[last][first]
    
        # print(ans)
    last-=1
    j+=1

    if j==len(matrix):
        i+=1
        j=0
        first+=1
        
        last=len(matrix)-1
matrix=ans
print(matrix)
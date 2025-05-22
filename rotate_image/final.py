from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        # transpose logic
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        print(matrix)
        # reverse the order of elements inside the matrix
        for row in matrix:
            row.reverse()
        
        return matrix
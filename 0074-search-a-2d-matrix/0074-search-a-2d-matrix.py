class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        n = len(matrix)
        m = len(matrix[0])

        low, high = 0, n*m-1
        while low<=high:
            mid = low + (high-low)//2
            row, col = mid//m, mid%m
            if(matrix[row][col]==target):
                return True
            elif(matrix[row][col]>target):
                high = mid - 1
            elif(matrix[row][col]<target):
                low = mid + 1
        return False
            
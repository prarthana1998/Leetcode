class Solution:
    def allCellsDistOrder(self, row: int, col: int, rCenter: int, cCenter: int):
       
       result = []

       for r in range(row):
        for c in range(col):
            result.append((r,c))

       result.sort(key=lambda x: abs(rCenter - x[0]) + abs(cCenter - x[1]))
       return result
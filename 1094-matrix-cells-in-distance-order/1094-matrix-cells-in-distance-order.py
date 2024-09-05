class Solution:
    def allCellsDistOrder(self, row: int, col: int, rCenter: int, cCenter: int):
        result = []
        for r in range(row):
            for c in range(col):
                # Append each cell's coordinates
                result.append([r, c])

        # Sort the result list by Manhattan distance to the center
        # Manhattan distance is |r - rCenter| + |c - cCenter|
        result.sort(key=lambda x: abs(x[0] - rCenter) + abs(x[1] - cCenter))

        return result
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rowLength, colLength = len(matrix), len(matrix[0])
        self.matrix = [[0 for _ in range(colLength)] for _ in range(rowLength)]
        for row in range(rowLength):
            self.matrix[row][0] = matrix[row][0]
            for col in range(1, colLength):
                self.matrix[row][col] = self.matrix[row][col-1] + matrix[row][col] 
        print(self.matrix)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sum = 0
        for row in range(row1, row2+1):
            beforeLeft = self.matrix[row][col1-1] if col1 > 0 else 0
            sum += self.matrix[row][col2] - beforeLeft
        return sum


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
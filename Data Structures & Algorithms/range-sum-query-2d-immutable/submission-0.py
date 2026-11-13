class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row_dif = row2-row1
        col_dif= col2-col1
        sum_return=0
        for i in self.matrix[row1:row2+1]:
            sum_return+=sum(i[col1:col2+1])
        return sum_return
                
                

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
__author__ = 'Zhijie Huang'

class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        m = len(matrix)
        n = 0
        if m:
            n = len(matrix[0])
        sums = [ [ 0 for j in range(n+1)] for i in range(m+1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                sums[i][j] = sums[i-1][j] + sums[i][j-1] - sums[i-1][j-1] + matrix[i-1][j-1]
        self.sums = sums

    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        result = self.sums[row2+1][col2+1] + self.sums[row1][col1] - self.sums[row1][col2+1] - self.sums[row2+1][col1]
        return result


# Your NumMatrix object will be instantiated and called as such:
# numMatrix = NumMatrix(matrix)
# numMatrix.sumRegion(0, 1, 2, 3)
# numMatrix.sumRegion(1, 2, 3, 4)
if __name__ == "__main__":
    matrix = [ [1,2,3,4], [5,6,7,8],[9,10,11,12],[13,14,15,16]]
    numMatrix = NumMatrix(matrix)
    print(numMatrix.sumRegion(0,1,2,3),numMatrix.sumRegion(1,2,3,3))


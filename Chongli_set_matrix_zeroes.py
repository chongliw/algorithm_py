__author__ = 'cwang'


class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        num_rows, num_cols = len(matrix), len(matrix[0])
        firstcol, firstrow = False, False
        for i in range(num_rows):
            for j in range(num_cols):
                if not matrix[i][j]:
                    if i and j:
                        matrix[i][0] = 0
                        matrix[0][j] = 0
                    if not i:
                        firstrow = True
                    if not j:
                        firstcol = True

        for i in range(1, num_rows):
            for j in range(1, num_cols):
                if not matrix[i][0] or not matrix[0][j]:
                    matrix[i][j] = 0
        if firstrow:
            for j in range(num_cols):
                matrix[0][j] = 0
        if firstcol:
            for i in range(num_rows):
                matrix[i][0] = 0


if __name__ == '__main__':
    test = Solution()
    matrix = [[0,0,0,5],[4,3,1,4],[0,1,1,4],[1,2,1,3],[0,0,1,1]]
    test.setZeroes(matrix)
    print(matrix)

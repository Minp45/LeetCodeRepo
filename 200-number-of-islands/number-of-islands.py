class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # first interate through the matrix and find the 1
        # if find i then use water flow method to change 1 to 0
        # if all the possibility is filled up increase the number for the number of islands

        num_island = 0
        row = len(grid)
        column = len(grid[0])

        def checkIsland(i, j):
            if i < 0 or j < 0 or i >= row or j >= column or grid[i][j] != '1':
                return
            grid[i][j] = '0'
            checkIsland(i - 1, j)
            checkIsland(i + 1, j)
            checkIsland(i, j - 1)
            checkIsland(i, j + 1)
        
        for i in range(row):
            for j in range(column):
                if grid[i][j] == '1':
                    num_island += 1
                    checkIsland(i, j)
        
        return num_island
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def check_around(i: int, j: int, grid: List[List[int]]) -> int:
            if(grid[i][j] == 1):
                grid[i][j] = 0
                sum = 1
                if(i < len(grid) - 1):
                    sum = sum + check_around(i + 1, j, grid)
                if(i > 0):
                    sum = sum + check_around(i - 1, j, grid)
                if(j > 0):
                    sum = sum + check_around(i, j - 1, grid)
                if(j < len(grid[0]) - 1):
                    sum = sum + check_around(i, j + 1, grid)
                return sum
            return 0
        highest = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j] == 1):
                    highest = max(highest, check_around(i, j, grid))
        return highest

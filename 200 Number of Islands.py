class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def crawl(i, j, grid) -> int:
            if(grid[i][j] == "1"):
                grid[i][j] = "0"
                if(i > 0):
                    crawl(i-1, j, grid)
                if(i < len(grid) - 1):
                    crawl(i+1, j, grid)
                if(j > 0):
                    crawl(i, j-1, grid)
                if(j < len(grid[0]) - 1):
                    crawl(i, j+1, grid)
                return 1
            return 0
        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                islands = islands + crawl(i, j, grid)
        return islands

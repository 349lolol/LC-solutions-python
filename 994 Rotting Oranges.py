class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        distance = [[-1 for j in range(len(grid[0]))] for i in range(len(grid))]
        q = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j]) == 2:
                    distance[i][j] = 0;
                    q.append((i, j))
        while len(q) > 0:
            i, j = q.popleft()
            if i > 0 and grid[i - 1][j] == 1 and distance[i - 1][j] == -1:
                distance[i - 1][j] = distance[i][j] + 1
                q.append((i - 1, j))
                grid[i - 1][j] = 2
            if i < len(grid) - 1 and grid[i + 1][j] == 1 and distance[i + 1][j] == -1:
                distance[i + 1][j] = distance[i][j] + 1
                q.append((i + 1, j))
                grid[i + 1][j] = 2
            if j > 0 and grid[i][j - 1] == 1 and distance[i][j - 1] == -1:
                distance[i][j - 1] = distance[i][j] + 1
                q.append((i, j - 1))
                grid[i][j - 1] = 2
            if j < len(grid[0]) - 1 and grid[i][j + 1] == 1 and distance[i][j + 1] == -1:
                distance[i][j + 1] = distance[i][j] + 1
                q.append((i, j + 1))
                grid[i][j + 1] = 2
        max_time = 0;
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j] == 1):
                    return -1
                if(grid[i][j] == 2):
                    max_time = max(max_time, distance[i][j])

        return max_time

        




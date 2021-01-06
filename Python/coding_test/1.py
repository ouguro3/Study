class Solution:
    def dfs(self, grid: List[List[str]], i: int, j: int):
        
        if i < 0 or i>= len(grid) or \
            j < 0 or j >= len(grid[0]) or \
            grid[i][j] != '1':
             return
        
        grid[i][j] = '0'
        
        self.dfs(grid, i+1, j)
        self.dfs(grid, i-1, j)
        self.dfs(grid, i, j+1)
        self.dfs(grid, i, j-1)
    
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    count += 1
        return count

# num_of_islands = Solution()
# print(num_of_islands.numIslands([["1","1","0","0","0"],["1","1","0","0","0"],
# ["0","0","1","0","0"],["0","0","0","1","1"]]))
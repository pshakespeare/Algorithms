


# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.


class Solution:
    visited = set()
    def find_islands(self,grid):
        if not grid:
            return 0

        ROW, COL = len(grid), len(grid[0])
        
        count = 0

        for r in range(ROW):
            for c in range(COL):
                if(grid[r][c] == "1" and (r,c) not in self.visited):
                    self.island_finder(grid, r, c)
                    count += 1
        return count           
    def island_finder(self,grid, i, j):
        if( i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != "1" or (i,j) in self.visited):
            return
            
        self.visited.add((i,j))
        self.island_finder(grid, i + 1, j)
        self.island_finder(grid, i - 1, j)
        self.island_finder(grid, i , j + 1)
        self.island_finder(grid, i, j - 1)


if __name__ == '__main__':
    solution = Solution()
    grid = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
    ]
    print(f"Number of islands: {solution.find_islands(grid=grid)} , Grid: {grid}")

class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def DFS(grid,i,j):
            if not 0 <= i < len(grid) or not 0 <= j < len(grid[0]) or grid[i][j] == 0:
                return 0

            grid[i][j] = 0

            Num = 1
            Num += DFS(grid,i+1,j)
            Num += DFS(grid,i-1,j)
            Num += DFS(grid,i,j+1)
            Num += DFS(grid,i,j-1)
            return Num


        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    ans = max(ans, DFS(grid,i,j))

        return ans

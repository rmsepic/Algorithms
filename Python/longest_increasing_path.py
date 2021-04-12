def longestIncreasingPath(matrix: List[List[int]]) -> int:
        def dfs(cur):
            if cur in table:
                return table[cur]

            length = 0
            for next_ in (cur + 1, cur - 1, cur + 1j, cur - 1j):
                if next_ in grid and grid[next_] > grid[cur]:
                     length = max(length, dfs(next_))

            table[cur] = 1 + length
            return table[cur]  
        
        table = {}
        grid = {x + y * 1j: value for y, row in enumerate(matrix) for x, value in enumerate(row)}
        
        return max( map(dfs, grid))
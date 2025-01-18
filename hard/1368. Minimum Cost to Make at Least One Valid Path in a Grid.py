class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
       
        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # right, left, down, up
        deque_ = deque([(0, 0, 0)])  # (x, y, cost)
        dist = [[float('inf')] * n for _ in range(m)]
        dist[0][0] = 0

        while deque_:
            x, y, cost = deque_.popleft()

            # If we've already found a lower cost for this cell, skip
            if cost > dist[x][y]:
                continue
            
            for d, (dx, dy) in enumerate(directions, start=1):
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    new_cost = cost if grid[x][y] == d else cost + 1
                    if new_cost < dist[nx][ny]:
                        dist[nx][ny] = new_cost
                        if grid[x][y] == d:
                            deque_.appendleft((nx, ny, new_cost))
                        else:
                            deque_.append((nx, ny, new_cost))
        
        return dist[m-1][n-1]

            
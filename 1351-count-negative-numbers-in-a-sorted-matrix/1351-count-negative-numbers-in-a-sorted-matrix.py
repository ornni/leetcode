class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        answer = 0
        for i in range(len(grid)):
            for j in grid[i]:
                if j < 0:
                    answer += 1
        return answer
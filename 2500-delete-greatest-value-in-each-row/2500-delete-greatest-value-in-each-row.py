class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        answer = 0
        
        for _ in range(len(grid[0])):
            Max = 0
            for i in grid[:]:
                i.sort()
                Max = max(Max, i.pop())
            answer += Max

        return answer

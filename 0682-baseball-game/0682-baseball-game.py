class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score = []
        for i in operations:
            if i == '+':
                score.append(score[-1] + score[-2])
            elif i == 'C':
                score.pop()
            elif i == 'D':
                score.append(score[-1] * 2)
            else:
                score.append(int(i))
        return sum(score)
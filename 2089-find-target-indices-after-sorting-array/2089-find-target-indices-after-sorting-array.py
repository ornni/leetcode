class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        answer = []
        nums.sort()
        index = 0
        
        for i in nums:
            if i == target:
                answer.append(index)
            index += 1
        
        return answer
        
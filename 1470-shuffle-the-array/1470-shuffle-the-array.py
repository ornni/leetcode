class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        index1 = 0
        index2 = n
        answer = []
        
        for i in range(len(nums) // 2):
            answer.append(nums[index1])
            answer.append(nums[index2])
            index1 += 1
            index2 += 1
        
        return answer

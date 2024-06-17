class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        answer = []
        index = 0

        for i in words:
            if x in i:
                answer.append(index)
            index += 1
        
        return answer
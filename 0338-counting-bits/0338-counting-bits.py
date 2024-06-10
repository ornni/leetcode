class Solution:
    def countBits(self, n: int) -> List[int]:
        answer = []
        for i in range(n+1):
            count = 0
            s = bin(i)[2:]
            for j in s:
                if j == '1':
                    count += 1
            answer.append(count)
        return answer
class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        answer = 0

        for i, j in zip(seats, students):
            answer += abs(i - j)
        
        return answer
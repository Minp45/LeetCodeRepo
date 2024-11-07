class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        # given the case where number of seats and students are always the same
        # then i will sort them, for both seats and students
        seats = sorted(seats)
        students = sorted(students)
        
        minimum_moves = 0 
        for i in range(len(seats)):
            print(seats[i], students[i])
            minimum_moves += abs(seats[i] - students[i])
        
        return minimum_moves


        # 3, 1, 5
        # 2, 7, 4

        # 1, 3, 5
        # 2, 4, 7
        # 1 + 1 + 2

        
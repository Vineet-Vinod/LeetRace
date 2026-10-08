class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        counts = [students.count(0), students.count(1)]
        for sandwich in sandwiches:
            if counts[sandwich] == 0:
                break
            counts[sandwich] -= 1
        return sum(counts)

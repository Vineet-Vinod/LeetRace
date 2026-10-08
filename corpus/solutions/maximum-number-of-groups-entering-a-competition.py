class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        groups = 0
        students = 0
        while students + groups + 1 <= len(grades):
            groups += 1
            students += groups
        return groups

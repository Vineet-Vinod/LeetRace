class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        total = sum(milestones)
        largest = max(milestones)
        remaining = total - largest
        return min(total, 2 * remaining + 1)

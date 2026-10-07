class Solution:
    def minimumChairs(self, s: str) -> int:
        occupied = 0
        maximum = 0
        for event in s:
            occupied += 1 if event == "E" else -1
            maximum = max(maximum, occupied)
        return maximum

class Solution:
    def busyStudent(
        self, startTime: list[int], endTime: list[int], queryTime: int
    ) -> int:
        return sum(start <= queryTime <= end for start, end in zip(startTime, endTime))

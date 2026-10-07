class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:
        width = len(seats[0])
        dp = {0: 0}
        for row in seats:
            usable = sum(1 << i for i, value in enumerate(row) if value == ".")
            valid = [
                mask
                for mask in range(1 << width)
                if mask & usable == mask and not mask & (mask << 1)
            ]
            dp = {
                mask: mask.bit_count()
                + max(
                    score
                    for previous, score in dp.items()
                    if not (mask & (previous << 1) or mask & (previous >> 1))
                )
                for mask in valid
            }
        return max(dp.values())

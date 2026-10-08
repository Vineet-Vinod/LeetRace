class Solution:
    def countDaysTogether(
        self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str
    ) -> int:
        month_start = (0, 0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334)

        def day_number(value: str) -> int:
            month, day = map(int, value.split("-"))
            return month_start[month] + day

        start = max(day_number(arriveAlice), day_number(arriveBob))
        end = min(day_number(leaveAlice), day_number(leaveBob))
        return max(0, end - start + 1)

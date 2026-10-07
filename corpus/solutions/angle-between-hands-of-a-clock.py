class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hour_position = (hour % 12) * 30 + minutes * 0.5
        minute_position = minutes * 6
        difference = abs(hour_position - minute_position)
        return min(difference, 360 - difference)

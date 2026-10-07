class Solution:
    def nextClosestTime(self, time: str) -> str:
        allowed = set(time.replace(":", ""))
        current = int(time[:2]) * 60 + int(time[3:])
        for elapsed in range(1, 24 * 60 + 1):
            minutes = (current + elapsed) % (24 * 60)
            candidate = f"{minutes // 60:02d}{minutes % 60:02d}"
            if all(digit in allowed for digit in candidate):
                return candidate[:2] + ":" + candidate[2:]
        return time

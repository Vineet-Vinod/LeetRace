class Solution:
    def numberOfRounds(self, loginTime: str, logoutTime: str) -> int:
        def minutes(stamp: str) -> int:
            hour, minute = map(int, stamp.split(":"))
            return hour * 60 + minute

        start = minutes(loginTime)
        end = minutes(logoutTime)
        if end < start:
            end += 24 * 60
        return max(0, end // 15 - (start + 14) // 15)

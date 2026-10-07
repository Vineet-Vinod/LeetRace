import datetime


class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        first = datetime.date.fromisoformat(date1)
        second = datetime.date.fromisoformat(date2)
        return abs((first - second).days)

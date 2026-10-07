class Solution:
    def dayOfYear(self, date: str) -> int:
        year, month, day = map(int, date.split("-"))
        before_month = (0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334)
        leap = year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
        return before_month[month - 1] + day + int(leap and month > 2)

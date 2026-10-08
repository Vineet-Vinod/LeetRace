class Solution:
    def reformatDate(self, date: str) -> str:
        day, month, year = date.split()
        months = {
            name: index
            for index, name in enumerate(
                (
                    "Jan",
                    "Feb",
                    "Mar",
                    "Apr",
                    "May",
                    "Jun",
                    "Jul",
                    "Aug",
                    "Sep",
                    "Oct",
                    "Nov",
                    "Dec",
                ),
                1,
            )
        }
        return f"{year}-{months[month]:02d}-{int(day[:-2]):02d}"

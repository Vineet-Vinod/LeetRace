class Solution:
    def findHighAccessEmployees(self, access_times: List[List[str]]) -> List[str]:
        by_employee: Dict[str, List[int]] = {}
        for name, time in access_times:
            minutes = int(time[:2]) * 60 + int(time[2:])
            by_employee.setdefault(name, []).append(minutes)
        result = []
        for name, times in by_employee.items():
            times.sort()
            if any(
                times[index + 2] - times[index] < 60 for index in range(len(times) - 2)
            ):
                result.append(name)
        return sorted(result)

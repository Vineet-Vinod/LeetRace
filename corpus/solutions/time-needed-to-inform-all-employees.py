class Solution:
    def numOfMinutes(
        self, n: int, headID: int, manager: List[int], informTime: List[int]
    ) -> int:
        children = [[] for _ in range(n)]
        for employee, boss in enumerate(manager):
            if boss != -1:
                children[boss].append(employee)
        longest = 0
        stack = [(headID, 0)]
        while stack:
            employee, elapsed = stack.pop()
            longest = max(longest, elapsed)
            for subordinate in children[employee]:
                stack.append((subordinate, elapsed + informTime[employee]))
        return longest

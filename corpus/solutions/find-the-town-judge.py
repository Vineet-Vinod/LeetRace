class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        balance = [0] * (n + 1)
        for person, trusted in trust:
            balance[person] -= 1
            balance[trusted] += 1
        for person in range(1, n + 1):
            if balance[person] == n - 1:
                return person
        return -1

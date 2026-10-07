class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        minutes: dict[int, set[int]] = defaultdict(set)
        for user, minute in logs:
            minutes[user].add(minute)
        answer = [0] * k
        for values in minutes.values():
            answer[len(values) - 1] += 1
        return answer

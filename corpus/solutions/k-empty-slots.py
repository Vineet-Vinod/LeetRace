class Solution:
    def kEmptySlots(self, bulbs: list[int], k: int) -> int:
        n = len(bulbs)
        if k + 1 >= n:
            return -1
        days = [0] * n
        for day, pos in enumerate(bulbs, 1):
            days[pos - 1] = day
        answer = n + 1
        left, right = 0, k + 1
        while right < n:
            i = left + 1
            while i < right and days[i] > max(days[left], days[right]):
                i += 1
            if i == right:
                answer = min(answer, max(days[left], days[right]))
                left = right
            else:
                left = i
            right = left + k + 1
        return answer if answer <= n else -1

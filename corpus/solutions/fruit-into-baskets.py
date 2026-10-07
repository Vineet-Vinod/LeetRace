class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        counts = defaultdict(int)
        left = 0
        best = 0
        for right, fruit in enumerate(fruits):
            counts[fruit] += 1
            while len(counts) > 2:
                outgoing = fruits[left]
                counts[outgoing] -= 1
                if counts[outgoing] == 0:
                    del counts[outgoing]
                left += 1
            best = max(best, right - left + 1)
        return best

class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        from collections import Counter

        counts = Counter(digits)
        result = []
        for value in range(100, 1000, 2):
            if not (Counter(map(int, str(value))) - counts):
                result.append(value)
        return result
